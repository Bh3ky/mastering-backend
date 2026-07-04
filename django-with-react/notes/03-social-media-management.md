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


## Writing the Post serializer

- the `Post` serializer will contain the fields needed to create a post when making a request on the endpoint. 
- in the `post` directory, add `serializer.py` file

- Django through `SlugRelatedField` field type handles the fields and relationship generation for us.
    - used to represent the target of the relationship using a field on the target, thus when creating a post, `public_id` of the author will be passed in the body of the request so that the user can be identified and linked to the post

- the `validated_author` method checks validation for the `author` field. 
    - here we are making sure that the user creating the post is the same user as in the `author` field.
    - a context dictionary is available in every serializer. usually contains the request object that we can use to make some checks.


## Writing Post viewsets

- for this endpoint, we ony allowing the `POST` and `GET` methods.

- our code should follow these rules:

    1. only authenticated users can create posts.
    2. only authenticated users can read posts.
    3. only `GET` and `POST` methods are allowed.

- inside the `core/post/` directory we create a new file `viewsets.py`

    - `get_queryset` method returns all the post.
    - `get_object` method returns a `post` using `public_id` that will be present in the URL. we retrieve this parameter from the `self.kwargs` directory.

    - the `create` method, which is the `ViewSet` action executed on `POST` requests on the endpoint linked to `ViewSet`. simply pass the data to the serializer declared on `ViewSet`, validate the data, and then call the `perform_create` method to create a `post` object. 

    - this method will automatically handle the creation of a `post` object by calling the `Serializer.create` method, which will trigger the creation of a `post` object in the database. finally, we return a response with the newly created post.


## Adding the Post route

- in the `routers.py` we add the new endpoint `/post/`.

- DRF provides a way to paginate responses and a default pagination limit size in the `settings.py`
- we can also use the `offset` parameter precisely to where we want the result to start from:

```text
GET https://api.example.org/accounts/?limit=100&offset=400
```

## Rewriting the Post serialized object

- in our current code, the `author` field accepts `public_id` and returns `public_id`. this does work, but it can be a little bit difficult to identify the user.

- the `to_representation()` method takes the object instance that requires serialization and returns a primitive representation [returns a built-in Python data types - the exact types which can be handled depend on the render class we configure for our API].

## Adding permissions

- authentication is an action of verifying the identity of a user, authorization is an action of checking whether the user has the rights or privileges to perform an action. 

in our project, we have three types of users:

- anonymous user (user with no account on the API and can't be identified)
- registered and active users (user has an account on the API and can easily perform some actions)
- admin user (user with all the rights and privileges)

- on our platform we want the anonymous users to be able to read the posts on the API without necessarily being authenticated. thus we need to write a custom permission.

- NB: Django permissions usually work on two levels: on the overall endpoint (`has_permission`) and on an object level (`has_object_permission`). 

- great way to write permissions is to always deny by default; that is why we always return `False` at the end of each permission method.

    - in the methods we have written so far, we are checking that anonymous users can only make the `SAFE_METHODS` requests - `GET`, `OPTIONS`, and `HEAD`.
    - and for other users, we are making sure that they are always authenticated before continuing.

## Deleting and updating posts

- to add these functionalities, we don't need to write serializer or viewset, as the methods for deletion [`destroy()`], and updating [`update()`] are already available by default in the `ViewSet` class.
- we just rewrite the `update` method on `PostSerializer` to ensure that the edited field is set to `True` when modifying a post.
    - add the `PUT` and `DELETE` methods to `http_methods` of `PostViewSet`

- NB: ended up implementing the soft delete feature instead.

## Adding the Like feature

- here we will be adding favouriting to our social media application.
- will also add data to count the number of likes a post has receieved and check whether a current user making the request has liked a post. 

Implemented in four steps:

1. add a new `posts_liked` field to the `User` model
2. write methods o nthe `User` model to like and remove a like from a post. will also add a method to check whether the user has liked a post.
3. add `likes_count` and `has_liked` to `PostSerializer`
4. add endpoints to like and dislike a post.

**Adding the `posts_liked` field to the User model

- the `posts_liked` field will contain all the posts liked by a user. the relationship between the `User` model and the `Post` model concerning the Like feature is:
    - a user can like many posts
    - a post can be liked by many users

This is a many-to-many relationship.

![new User table structure](image-1.png)

