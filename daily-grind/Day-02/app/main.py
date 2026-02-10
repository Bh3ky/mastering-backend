from fastapi import FastAPI, APIRouter
from routers.items import router as items_router

# instantiate the app
app = FastAPI()

# create the router
api_v1_router = APIRouter(prefix="/api/v1")

@api_v1_router.get("/health")
def health_check():
    return {"status": "ok"}

# register the router with the app
api_v1_router.include_router(items_router)
app.include_router(api_v1_router)

