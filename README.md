# Mastering Backend with Python

A hands-on, project-based roadmap for becoming a strong backend engineer with Python.

The repository is organised as a collection of focused projects and study tracks. Each one targets a different part of backend development, and they grow in complexity over time. The goal is depth of understanding rather than speed: clean architecture, async systems, background workers, production-ready services, testing and deployment.

For the full list of topics being covered, see [ROADMAP.md](ROADMAP.md).


## Repository Structure

```
mastering-backend/
├── core-api-platform/           # FastAPI fundamentals
├── async-event-system/          # FastAPI + Celery + async workflows
├── production-backend-service/  # Django, production-style backend
├── django-with-react/           # Full-stack Django REST API + React client
├── modern-django-web-dev/       # Django from first principles (book study + code)
├── object-oriented-programming/ # OOP study notes and practice projects
├── PROJECTS/                    # Standalone practice projects (e.g. banking-system-cli)
├── daily-grind/                 # Daily Python practice exercises
├── books/                       # Reference material
├── ROADMAP.md                   # Skills checklist
└── setup.sh                     # Environment bootstrap script
```

Most folders are self-contained, with their own dependencies and, where applicable, their own README.


## Projects

### Core API Platform (FastAPI)

Focus: REST APIs, request/response lifecycle, validation with Pydantic, authentication, pagination, filtering, testing and API docs.

Tech: FastAPI, Uvicorn, Pydantic, Pytest

### Async Event System (FastAPI + Celery)

Focus: background tasks, queues and workers, event-driven design and asynchronous processing.

Tech: FastAPI, Celery, Redis, Uvicorn

### Production Backend Service (Django)

Focus: full-stack backend structure, the Django ORM and admin, authentication and permissions, and real-world patterns.

Tech: Django, Django REST Framework (planned), PostgreSQL (planned)

### Django with React

Focus: building a social media application with a Django REST API (JWT authentication, posts, comments, testing) and a React frontend. Chapter notes are in `django-with-react/notes`.

Tech: Django, Django REST Framework, JWT, React, Pytest


## Study Tracks

### Modern Django Web Development

Working through *Modern Django Web Development* from first principles. Each chapter has written notes and accompanying code (`firstproject`, `firstapp`) covering projects, apps, views, URL routing, templates and the admin.

### Object-Oriented Programming

Structured notes and practice projects covering classes and objects, abstraction, encapsulation, inheritance, polymorphism and design principles.

### Practice Projects and Daily Exercises

- `PROJECTS/banking-system-cli`: a command-line banking system with tests and an architecture write-up.
- `daily-grind`: short daily exercises to build consistency with Python fundamentals.


## Getting Started

```bash
git clone https://github.com/Bh3ky/mastering-backend.git
cd mastering-backend
```

Each project manages its own dependencies. Create a virtual environment inside the project you want to run and install from its `requirements.txt`:

```bash
cd <project-folder>
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Refer to each project's README for run instructions.


## Philosophy

- Learn deeply, not quickly
- Build things that can grow
- Learn by making mistakes and fixing them
- Write code that is understandable six months later


## License

Licensed under the MIT License.
