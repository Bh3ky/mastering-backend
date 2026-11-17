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


# One-to-One Relationship
class College(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Principal(models.Model):
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)

    college = models.OneToOneField(
        College,
        on_delete=models.CASCADE,
        related_name="principal"
    )

    def __str__(self):
        return self.name


# One-to-Many Relationship
class Subject(models.Model):
    name = models.CharField(max_length=30)
    credits = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="teachers"
    )

    def __str__(self):
        return self.name


# Many-to-Many Relationship
class Course(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(
        Teacher,
        related_name="courses"
    )

    def __str__(self):
        return self.name