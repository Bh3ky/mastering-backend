# Mastering Backend with Python

This repository is my 6-month roadmap to mastering backend development using Python.
It’s structured as a series of evolving projects, each focused on a different backend architecture and skill set.

The goal is not just to “finish” projects, but to grow them gradually while learning:

* Clean architecture
* Async systems
* Background workers
* Production-ready backends
* Testing, config, and deployment thinking



## Structure

```
mastering-backend/
├── core-api-platform/          # FastAPI fundamentals
├── async-event-system/         # FastAPI + Celery + async workflows
└── production-backend-service/ # Django, production-style backend
```

Each folder is its own isolated project with:

* Separate virtual environment
* Independent dependencies
* Its own README and roadmap
* Room to grow over time



## Projects

### 1. Core API Platform (FastAPI)

Focus:

* REST APIs
* Request/response lifecycle
* Validation with Pydantic
* Auth, pagination, filtering
* Testing and docs

Tech:

* FastAPI
* Uvicorn
* Pydantic
* Pytest



### 2. Async Event System (FastAPI + Celery)

Focus:

* Background tasks
* Queues and workers
* Event-driven design
* Async processing

Tech:

* FastAPI
* Celery
* Redis
* Uvicorn



### 3. Production Backend Service (Django)

Focus:

* Full-stack backend structure
* Django ORM and admin
* Authentication & permissions
* Real-world patterns

Tech:

* Django
* Django REST Framework (later)
* PostgreSQL (later)



## Philosophy

This repo is about:

* Learning deeply, not quickly
* Building things that can grow
* Making mistakes and fixing them
* Writing code that I can understand 6 months later

Each project will start small and become more complex over time.



## How to Use This Repo

* Each folder can be treated like its own repo
* Each has its own setup and instructions
* Root is just an overview and organizer

## License

- Licensed under MIT
