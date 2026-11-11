# Chapter 02

## Django Project

Django auto-generates a file `settings.py` which defines the default values of a number of parameters such as installed apps, database configuration, URL dispatcher etc.

Other Python modules in the project package folder:

1. `settings.py` - Django creates this script with certain default values of various params such as database connection, URLCONF path, location of templates and static assets.
2. `urls.py` - also called URLCONF. Django uses this script to locate the view that matches with the request URL. NB: the urlpatterns of all apps are registered with the URLCONF of the project.
3. `wsgi.py` - this module uses the project's settings and returns a WSGI application object. any WSGI-compatible server can use this object to serve the application
4. `asgi.py` - this module is the entry point for ASGI-compatible web servers such as Uvicorn or Daphne to server the project.

The file `manage.py` in the root folder acts as a local copy of the django-admin command-line utility.

- all the admin tasks that `django-admin` can perform can be done with `manage.py` script.
- more suited for a single project. `djang-admin` utility is more convenient when the application involves multiple Django projects.

## Django App

The Django project is a complete web application whose functionality may have multiple submodules.

- in Django parlance, the submodules are called apps.

**Define views**

In the View layer in Django's MVT architecture is where the processing logic is defined. 

- a view is a Python function or a class that has been assigned the job to process the incoming request and formulate an appropriate response to be returned to the client.
- our functions are added to the `views.py` file/module.

The Django server provides the `HttpRequest` object as an argument to a view function, which returns an object of `HttpResponse` class (defined in the `django.http` module).

**Define urlpatterns**

The URL pattern is a mapping of a view to its desired request URL.

- typically, urlpatterns are defined in a `urls.py` module in the app package folder.
- the `path()` function defined in the `django.urls` module creates the association of a URL route with the view function.

    `path(route, view, kwargs=None, name=None)`

The route argument is a string representing the URL pattern. The string contains the tailing path_info part of the URL, excluding the hostname and the prefix e.g., `http://localhost:8000/firstapp/about/`

- `firstapp` - the prefix after the hostname
- `about/` - route argument

The view argument is the name of the function in the `views.py` module.

- the `about/` route is mapped to the `views.about()` function.

NB: The name argument should also be provided as it proves useful in forming named urlpatterns.

**Update URLCONF**

The `urls.py` module in the project package is referred to as URLCONF.

- it includes the urlpatterns of all the installed apps in the project. 

    - when a client request is received, Django locates a matching view function from the registered patterns.
- we need to include the urlpatterns of the app (`firstapp/urls.py`) in the URLCONFIG of the project (`firstproject/urls`). 
- the `include()` function from `django.urls` module does this job.

**Path Parameters**
