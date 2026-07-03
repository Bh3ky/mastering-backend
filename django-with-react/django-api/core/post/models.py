from django.db import models

from core.abstract.models import AbstractModel, AbstractManager


class PostManager(AbstractManager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class Post(AbstractModel):
    author = models.ForeignKey(to="core_user.User", on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = PostManager()
    all_objects = AbstractManager()

    def __str__(self):
        return f"{self.author.name}"
    

    class Meta:
        db_table = "core.post"

