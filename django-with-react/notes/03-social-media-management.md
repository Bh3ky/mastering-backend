# Social Media Post Management

## Creating the Post model

- a post in this project is a long or short piece of text that can be viewed by anyone, irrespective of whether a user is linked or associated to that post.

Post feature requirements
    - authenticated users should be able to create a post
    - authenticated users should be able to like the post
    - all users should be able to read the post, even if they are not authenticated
    - the author of the post should be able to modify the post
    - the author of the post should be able to delete the posts

- from these requirements, we will mostly be dealing with a database, model, and permissions.

## Designing the Post model

- a post consists of content made up of characters written by an author; in this case a user, so how does that schematize itself into the database??

![post table](image.png)

- we have an `author` field, which is a **foreign key**.

**Question: what is a foreign key??**
- a foreign key is a set of attributes in a table that refers to the primary key of another table.

- in our case, the foreign key will refer to the primary key of the `User` table. each time a post is created, a foreign key will need to be passed.

- we will use **one-to-many** relationship i.e., a user (from the `User` table) can have many posts (in the `Post` table), and thus a post can only belong to a single user.

- and the **many-to-many** relationship will be used on the like feature for the posts.


## Abstraction

- an abstract class can be considered a blueprint for other classes. it usually contains a set of methods or attributes that must be created within any child classes built from the abstract class.

- for our `public_id`, `created`, and `updated` fields we will use abstract model class.

- inside the `core/` directory, we add a new `abstract/` Python package and inside add a file `models.py` and write two classes: `AbstractModel` and `AbstractManager`
    - the `AbstractManager` class contains the function for retrieving an object by its `public_id` and the `AbstractModel` contains fields `public_id`, `created`, and `updated`.

- NB: in our `Meta` class we set `abstract = True`, thus Django will ignore this class model and won't generate migrations for it.

- next, we modify our `core/user/models.py` file to remove the `get_object_by_public_id` method and subclass `UserManager`


