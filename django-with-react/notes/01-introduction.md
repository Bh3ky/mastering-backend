# Introduction: Django

Software development is a multi-step process which involves a lot of components. these components ensure that conceiving, specifying, designing, programming, documenting, and testing an application, framework, or software is well applied.

**Understanding backend development**

- backend development handles the behind-the-scenes of modern applications. oftenly made up of code that connects to the database, manages user connections, and also powers web applications or the API.

- backend development mostly focuses on the business logic of the code i.e., how an application works, the functionality, and logic powering it.


**Responsibilities of backend developers**

1. **server** which is a machine or an application (NGINX) that receives requests
2. **application** which is a running application on the server that receives the requests, validates these requests, and sends an appropriate response
3. **database** which is used to store data

- in simple terms the responsibilities of backend programmers mainly involve writing APIs, writing code to interact with a database, creating modules or libraries, also working on business data and architecture and much more.


**What is an API**

- an API simplifies the way daya is exchanged between applications or machines. consists mainly of two components:
    1. the technical specification, which describes the data exchange options between parties with the specification made in the form of a request for data delivery protocols and data processing.
    2. the software interface (the programming code), which is written to the specification that represents it.

**Terms**

- remote procedure call (RPC) - a protocol that can be used by a program to request a service from a program on another computer on a network that it doesn't need to know the details of. sometimes called a _function or subroutine call_.

- simple object access protocol (SOAP) - an XML-based communication protocol that allows applications to exchange information with each other over HTTP.

- REST/RESTful - a style of architecture for building applications (web, intranet, or web services). NOTE: this is a set of conventions and best practices to be observed, not a technology on its own right.
    - the REST architecture uses the original specifications of the HTTP protocol, rather than reinventing an overlay.:
        1. URL  is a reource identifier
        2. HTTP verbs are identifiers of operations
        3. HTTP responses are representation of resources
        4. links are relations between resources
        5. parameter is an authentication token


**Understanding REST APIs**

- REST makes it easier to write the logic to access resources; resources here are represented by a unique URL available with one request to this URL.

- REST APIs use HTTP requests (or methods) to interact with resources:
    1. GET - used to retrieve data from a server at a specified resource. this resource is an endpoint returning an object or a list of objects in JSON or XML most of the time. 

    2. POST - method for requesting information processing from the server. the data to be processed is specified in the body of the request and the document designated by the request via the page is the resource that must process the data and generate the response.

    3. HEAD - method used to query the header of the response, without the file being sent to us immediately. 

    4. OPTIONS - diagnostic method, which returns a message that is useful primarily for debugging etc. 

    5. DELETE and PUT - methods which allow a document to be uploaded (to the server) or deleted without going through a File Transfer Protocol (FTP) server. NOTE: most web servers require a special configuration with a resource or document responsible for processing these requests.

    6. PATCH - method of an HTTP requests which applies partial changes to a resource.

    7. TRACE - method that can be ysed to trace the path that an HTTP request takes to the server and then to the client.

    8 CONNECT - used to request the use of the server as a proxy.

RESTful systems support different data formats such as plain text, HTML, YAML, JSON, and XML


## Django

**What is Django??**

- it is an advanced web framework written in Python which makes the use of the Model-View-Controller (MVC) architecture pattern.
    - model - corresponds to all the data-related logic. it's deeply connected to the database, as it provides the shape of the data but also methods and functions for Create, Read, Update, and Delete (CRUD) operations.

    - view - handles the UI logic of the application

    - Controller - represents a layer between the model and view. most of the time, controllers interpret the incoming requests from the view, manipulate the data provided by the model compoment, and interact with the view again to render the final output. 


Model-View-Template (MVT)


## Setting up working environment

- to create a new project in Django we use the `django-admin` command:

```bash
django-admin startproject <name> .
```

- then we run a migration command:

```bash
python manage.py migrate
```

- NB: migrations are a way to propagate changes made to the model (such as **User** used for authentication) in the database schema.

- Django had **object-relational mapping (ORM)** that automatically handles the interaction with the database. 
    - ORM is basically a technique for mapping models to the relational database using Python.

**Files in our directory**

1. `manage.py` - is a utility provided by Django which helps us create projects and applications, run migrations, start a server etc. 

2. `CoreRoot/` - is the project we created using the `django-admin` command. contains the following files:
    - `urls.py` - contains all the URLs that will be used to access resources in the project

    ```python
    from django.contrib import admin
    from django.urls import path

    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
    ```

    - `wsgi.py` - used for deployment but also the default development environment in Django.
    - `asgi.py` - Django supports running asynchronous code as an ASGI application
    - `settings.py` - contains all the configurations for the Django project. here we can find `SECRET_KEY`, the `INSTALLED_APPS` list, `ALLOWED_HOST` etc.