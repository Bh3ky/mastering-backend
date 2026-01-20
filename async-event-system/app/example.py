from app.celery_app import celery

@celery.task
def add_task(a, b):
    return a + b
