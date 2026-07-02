# Authentication and Authorization using JWTs


**Understanding JWTs**

- JWT stands for JSON Web Token.
- it's a JSON object defined as a safe way of transmitting information between two parties.
    - information transmitted by JWT is digitally signed so it can be verified and trusted.

- JWT contains three parts:
    1. header (x)
    2. payload (y)
    3. signature (z) all separated by a dot.

1. **Header**

- the header of the JWT consists of two parts:
    - type of token
    - signing algorithm being used [used to ensure that the message is authenticated and not altered] e.g.,

    ```text
    {
        "alg": "RSA",
        "typ": "JWT
    }
    ```

    - signing algorithms are used to sign tokens issued for the application or API.

2. **Payload**

- is the second part which contains the claims [which are statements about an entity typically the user & additional data].

    ```text
    {
        id": "d1397699-f37b-4de0-8e00-948fa8e9bf2c",
        "name": "John Doe",
        "admin": true 
    }
    ```

    - we have three claims here: user ID, name of user, and Boolean for the type of user.

3. **Signature**

- it is the encoded header, the encoded payload plus a secret, and an algorithm specified in the header e.g., using RSA algorithm:

```bash
RSA(
    base64UrlEncode(header) + "." +
    base64UrlEncode(payload),
    secret)
```

- NB: the signature tracks whether the information has been changed.


**How JWTs are used in authentication??**

- every time a user successfully logs in, a JWT is created and returned. 
- the JWT is presented as credentials used to access protected resources. 
- NOTE: JWT expiration should be capped (should have short lifespan) to curb vulnerabilities.

Types of tokens:

1. access token - used to access resources and handle authorization.
2. refresh token - used to retrieve a new access token. 

    - NB: refresh token contains essential information needed to verify the user and generate a new access token. 

## Organising a project

- when working with Django, we have the ability to create many apps to handle different parts of the project.
- to create a Django application we run:

```bash
django-admin startapp core
```

## Creating a user model


**Django models**

- Django models provide **object-relational mapping (ORM)** to the underlying databse. 
    - ORM is a tool that simplifies database programming by providing a simple mapping between the object and the database.
    - it abstracts us from being worried about the database structure or writing complex SQL queries to manipulate or retrieve data from the database.

- advantages of writing models with Django:
    1. simplicity
    2. consistency
    3. tracking

- Django Manger is a class which behaves as an interface through which Django models interact with databases.
    - every Django model inherits the `models.Manager` class by default that comes with the necessary methods to make **Create, Read, Update, and Delete(CRUD)** operations on the table in the database

## Writing the User model

- Django comes a pre-built-in **User** model that we can use for basic authentication or a session. 
    - it provides authentication feature we can use to quickly add authentication and authorization to our projects. 

What is a superuser?
- a user with administrator permission.

What is a Django application?
- it's a submodule of a Django project or a Python package structured to work in a Django project and share Django conventions such as containing files or submodules such as `models`, `tests`, `urls`, and `views`.

- the `models` module from Django some field utilities that can be used to write fields and add some rules e.g.,:
    - `CharField` - represents the type of field to create in the `User` table similar to `BooleanField`.
    - `EmailField` is also `CharField` but rewritten to validate the email that is passed as a value to this field.

- NB: `EMAIL_FIELD` and `USERNAME_FIELD` are set as email and username to respectively to provide two fields for login.

- `name` method is basically a model property, which can be accessed anywhere on a `User` object, such as `User.name`

- `__str__` method is rewritten to return a string which can help us quickly identify a `User` object.


## Creating the user and superuser

- for the `create_user` method, we make sure that the fields such as `password`, `email`, `username`, `first_name`, `last_name` are not None. 

- we use `save()` method to save the user in the table if everything is correct in the model.

- after this stage, we register the user application in the `CoreRoot/settings,py` and then run migrations to create the table in the database.

- also need to tell Django to use this `User` model for the authentication user model. in `CoreRoot/settings.py` we add:

```python
AUTH_USER_MODEL = 'core_user.User'
```


## Writing UserSerializer

- a serializer allows us to convert complex Django data structures such as `QuerySet` or model instances into Python native objects that can be easily converted to JSON or XML format.
- a serializer can also serialize JSON or XML to native Python

**Django Rest Framework (DRF)** provides a `serializers` package that we can use to write serializers and also validations when API calls are made to an endpoint using this serializer. 

- command for installing the DRF:

```bash
pip install djangorestframework django-filter
```

- then we add `rest_framework` to the `INSTALLED_APPS` setting.

- we create a file `serializers.py` in the `core/user` directory and write our `UserSerializer` class

- the `UserSerializer` class inherits from the `serializers.ModelSerializer` class. it's a class inheriting from the `serializers.Serializer` class but has deep integrations for supporting a model. it automatically matches the field of the model to the correct validation.

    - e.g., since we specified that the email is unique, when someone tries to register with an email that already exists in the database, they receive an error message.

- the `fields` attribut contains all the fields that can be read or written. 


## Writing UserViewset

- since Django is based on **Model-View-Template** architecture, the model can communicate with the views (or controllers) and the template displays responses or redirects requests to the views.

- however, when Django is coupled with DRF, the model can be directly connected to the view. NB: it's always recommended to use a serializer between a model and a viewset. why??
    - helps with validation and some checks

**What is a viewset??**
- a viewset is simply a class-based view that can handle all the basic HTTP requests—`GET`, `POST`, `PUT`, `DELETE`, and `PATCH`—without hardcoding any CRUD logic.

- DRF provides a class named `APIView` from which a lot of classes from DRF inherit to perform CRUD operations.

- for the `viewset` user, we only allowing the `PATCH` and `GET` methods. the endpoints:


|Method | URL | Result |
| --- | --- | --- |
| `GET`| `/api/user/` | List all the users |
| `GET` | `/api/user/user_pk` | Retrieves a specific user |
| `PATCH` | `/api/user/user_pk` | Modifies a user |

- `serializer_class` and `permission_classes` to `AllowAny` and they can be accessed by anybody.

two methods:

1. `get_queryset` - used by the viewset to get a list of all the users. this method will be called when `/user/` is hit with a `GET` request.

2. `get_object` - this method is used by the viewset to get one user. it is called when a `GET` or `PUT` request is made on the `/user/id/` endpoint, with `id` representing the ID of the user.


## Adding a router

- routers allow us to quickly declare all of the common routes for a given controller.

- REST framework adds support for automatic URL routing to Django, and provides you with a simple, quick and consistent way of wiring your view logic to a set of URLs.

- at the root of the apps project (`core`) we add a file `routers.py`:

    - to register a route for a viewset, the `register()` method needs two arguments:
        1. prefix - representing the name of the endpoint.
        2. viewset - only representing a valid viewset class.

    - NB: `basename` argument is optional but it's good practice to use one. helps for readability and also helps Django registry purposes.
        - the base to use for the URL names that are created. if unset the `basename` will be automatically generated based on the queryset attribute of the viewset, if it has one. NB that if the viewset does not include a queryset attribute then must set `basename` when registering the viewset.

- NOTE: now that the user route is working, we need to change the permission so that users don't send requests to modify their name using `PATCH` requests.
    - change the permission on the `permission_classes` attribute in the `UserViewSet` class.


## Writing the user registration feature

- before accessing protected data, the user needs to be authenticated, provided they have an account and credentials.

- register the app in `INSTALLED_APPS` and specify `DEFAULT_AUTHENTICATION_CLASSES` in the `REST_FRAMEWORK` dict.

- we create a new app called `auth` which contains the logic for login, logout, etc
    - inside this app we add `serializers/` and `viewsets/` folders


## Adding the login feature

- the login feature requires the email or username with the password. in order to do so we use our `djangorestframework-simplejwt` package, which provides a serializer called `TokenObtainPairSerializer`.
    - we write a serializer to check for user authentication but also return a response containing access and refresh tokens. 
        - to do this we have to rewrite the validate method from `TokenObtainPairSerializer` class.
- add a `login.py` file inside the `core/auth/serializer` directory.

- NB: we use `super()`, which is a built-in method in Python that returns temporary object that can be used to access the class methods of the base class. basically, we are surcharging the `validate` method from the `TokenObtainPairSerializer` class to adapt it to our needs.

- after this we add a `LoginViewSet`. since we are not directly interacting with a model here, we will just use the `viewsets.ViewSet` class

- the login features works for now but it's not perfect. the access token expires in 5 minutes. we need to fix this????


## Refresh logic

- `djangorestframework-simplejwt` provides a refresh logic feature. 
- since we have been generating refresh tokens and returning them as responses every time registration or login is completed, we will just inherit the class from `TokenRefreshView` and transform it into a viewset.

    - add `refresh.py` file inside `auth/viewsets`



**Question: what is a JWT??**
- a **JSON Web Token (JWT)** is a compact, signed token that provides a user's identity after they authenticate.

**Question: what is Django Rest Framework??**
- Django framework for building RESTful APIs

**Question: what is a model??**
- a model defines how data is stored in the database.

**Question: what is a serializer??**
- a serializer converts between Python objects and JSON while also validating incoming data.

**Question: what is a viewset??**
- defines the business logic for API endpoints [essentially the API controlller].

**Question: what is a router??**
- a router automatically maps URLs to ViewSet methods

**Question: what is a refresh token??**
- a refresh token is used to obtain a new access token adter the current access token expires.

