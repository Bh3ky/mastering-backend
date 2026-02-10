from fastapi import APIRouter, Query, HTTPException
from typing import Optional

# items router
router = APIRouter(prefix="/items", tags=["items"])

@router.get(
        "/",
        summary="List items",
        description="Retrieve a list of items with optional filtering, sorting, and pagination.")
def list_items(
    page: int = Query(
        1, ge=1,
        description="Page number, starting from 1"
    ),
    limit: int = Query(
        10, ge=1, le=100,
        description="Number of items per page"
    ),
    name: Optional[str] = Query(
        None, description="Filter items by name (case-insensitive substring)"
    ),
    sort_by: str = Query(
        "id", description="Filter to sort by (id or name)"
    ),
    order: str = Query(
        "asc", description="Sort order: ascending (asc) or descending (desc)"
        )
):
    items = [
        {"id": 1, "name": "Notebook"},
        {"id": 2, "name": "Pen"},
        {"id": 3, "name": "Pencil"},
        {"id": 4, "name": "Eraser"},
        {"id": 5, "name": "Marker"},
    ]

    if name is not None:
        items = [
            item for item in items
            if name.lower() in item["name"].lower()
        ]

    allowed_sort_fields = {"id", "name"}
    allowed_order_values = {"asc", "desc"}

    if sort_by not in allowed_sort_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}")
    
    if order not in allowed_order_values:
        raise HTTPException(status_code=400, detail=f"Invalid sort order: {order}")
    
    reverse = order == "desc"

    items = sorted(
        items,
        key=lambda item: item[sort_by],
        reverse=reverse,
    )

    total = len(items)

    start = (page - 1) * limit
    end = start + limit
    paginated_items = items[start:end]

    return {
        "data": paginated_items,
        "meta": {
            "total": total,
            "page": page,
            "limit": limit,
        },
    }