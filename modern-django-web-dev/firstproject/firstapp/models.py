from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    publisher = models.CharField(max_length=50)

    # add metadata of the model
    class Meta:
        db_table = "books"

    def __str__(self):
        return f"Title : {self.title} | Author : {self.author} | Price : {self.price}"