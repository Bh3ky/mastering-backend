#!/bin/bash

projects=(
    "core-api-platform"
    "async-event-system"
    "production-backend-service"
)

for p in "${projects[@]}"; do
    echo "---- Setting up $p ----"

    # Create folder if missing
    if [ ! -d "$p" ]; then
        echo "Creating $p"
        mkdir -p "$p"
    fi

    cd "$p" || exit

    # Create venv if missing
    if [ ! -d ".venv" ]; then
        python3 -m venv .venv
    fi

    source .venv/bin/activate

    # Install only if requirements exist
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        echo "No requirements.txt in $p yet – skipping install"
    fi

    deactivate
    cd ..
done

echo "All projects initialized."
