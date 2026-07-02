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


## Writing the AbstractSerializer

- all the objects sent back as a response in our API will contain the `id`, `created`, and `updated` fields. in order not to write these fields all over again on every `ModelSerializer`, we just create an `AbstractSerializer` class.
    - in the `abstract/` directory, we create a file `serializer.py`.
    - then we subclass the `UserSerializer` class with the `AbstractSerializer` class in `core/user/serializers.py` and remove `id`, `created`, and `updated`.

## Writing the AbstractViewSet

- why do we need an abstract `ViewSet`?? because there will be repeated declarations as to the ordering and the filtering. 
    - now we create a class that contains the default values.
    - in the `core/abstract/` we create a file `viewsets.py.

- then we add the `AbstractViewSet` class to the code where `ModelViewSets` is actually called. directory `core/user/viewsets.py`

## Writing the Post model

Core feautes:

1. new application called `post/`
2. rewrite `apps.py`
3. `Post` model in `core/post/models.py`

- here we create the `ForeignKey` relationship. Django models provide tools to handle this kind of relationship, and it is also symmetrical i.e., not only can we use the `Post.author` syntax to access the user object, but we can also access posts created by a user using the `User.post_set` syntax.

- NB: the latter syntax will return a `queryset` object containing the posts created by the user because we are in a `ForeignKey` relationship [which is one-to-many]. 

- on the `on_delete` attribute with the `models.CASCADE` value, we used `CASCADE` why?? so that when a user is deleted from the database, Django will also delete all records of posts in relation to this user.


- NB: apart from `CASCADE` as a value for the `on_delete` attribute on a `ForeignKey` relationship, we can also have the following
    - `SET_NULL` - this sets the child object foreign key to null on delete.
    
    - `SET_DEFAULT` - sets the child object to the default value given while writing the model.

    - `RESTRICT` - raises `RestrictedError` under certain conditions.

    - `PROTECT` - prevents the foreign key object from being deleted as long as there are objects linked to the foreign key object.