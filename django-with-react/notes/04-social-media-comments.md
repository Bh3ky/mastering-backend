# Adding Comments to Social Media Posts

## Writing the Comment model

- a comment in context of this project represents a small text that can be viewed by anyone but only be created or updated by authenticated users.

![comment table structure](image-2.png)

A comment will mostly have four components:

1. author of the comment
2. post on which the comment has been made
3. body of the comment
4. edited field to track whether the comment has been edited or not

- here we can see that we have two database relationships in the table: author and post. how does this schematize in the database?

![comment, post, and user relationshops](image-3.png)

- here, the author (`User`) and post (`Post`) fields are **ForeignKey** types. some rules for the comment feature:

    1. a user can have many comments, but a comment is created by one user
    2. a post can have many comments, but a comment is linked to only one post

**Adding the Comment model**

- `core/comment/models.py/` directory:

## Writing the comment serializer

- the comment serializer will help with validation and content creation. 

- write `CommentSerializer` in the `/core/comment/serializers.py`

To create a comment, we need three fields:
    - `public_id` of the author
    - `public_id` of the post
    - the body

- also add validation methods for the `author` field.

- in `validate_author` we block users from creating comments for other users.
- `to_representation` method modifies the final object by adding information about the author.

## Nesting routes for the comment resource

- to create, update, or delete comments, we need to add `ViewSet`. file directory: `comment/viewsets.py`

**Endpoint architecture**

| Method  | URL           | Result           |
| ---     | ---           | ---              |
| `GET`   | `/api/post/post_pk/comment/` | Lists all the comments related to a post |
| `GET`   | `/api/post/post_pk/comment/comment_pk/` | Retrieves a specific comment |
| `POST`  | `/api/post/post_pk/comment/` | Creates a comment |
| `PUT`   | `api/post/post_pk/comment/comment_pk/` | Modifies a comment |
| `DELETE` | `api/post/post_pk/comment/comment_pk` | Deletes a comment |

- in the given structure above, the endpoint is nested i.e., the commment resources live under post resources.

- Django library `drf-nested-routers` helps us write routers to create nested resources. 

## Creating nested routes

- modify `core/routers.py` file

`NestedSimpleRouter` is a sub-class of the `SimpleRouter` class, which takes initialization params such as `parent_router - router -parent_prefix - r'post' - and the lookup -post`. the lookup is the regex variable that matches an instance of the parent resource `-PostViewSet`.

- the lookup regex is `post_pk`

- now we register the `comment` route on `post_router`

## Writing the CommentViewSet class

- `get_queryset()` method is called when the user hits the endpoint `api/post/post_pk/comment/`. the first verification here is to check whether the user is a superuser and if that is the case, we return all the comment objects in the database.
- if the user is not a superuser, then we return the comments concerning a post. 
    - with the post nested route, we set the `lookup` attribute to `post` i.e., in `kwargs` (a dictionary containing additional data) of every request, a public id value of the `post` with the dictionary key `post_pk` will be passed in the URL of the endpoint.
- and if that's not the case we just return a 404

- we then make a query to the database by filtering and retrieving only comments that have the `post.public_id` field equal to `post_pk`. 
    - this is done with the filter method provided by the Django ORM. it's useful to write conditions for retrieving objects from the database.

- then we add the `get_object` method to the same `CommentViewSet` so we can use the `public_id` to retrieve the specific comment.
    - the method is called on each request made to the `/api/post/post_pk/comment/comment_pk/` endpoint. NB the `pk` is represented by `comment_pk`. 
    - then we retrieve the object and check for permissions. if everything is goos, we return the object

- write the `create` method where we pass `request.data` to the `ViewSet` serializer - `CommentSerializer` - and try to validate the serializer. if everything is good, we move to create a new object - a new comment - based on the serializer from `CommentSerializer`.

## Updating a comment

- updating a comment is an action that can only be done by the author of the comment. the user should only be able to update the body field of the comment and can't modify the author value.

## Deling a comment

- deleting a comment is an action that can only be performed by the author of the post, the author of the comment, and a superuser.