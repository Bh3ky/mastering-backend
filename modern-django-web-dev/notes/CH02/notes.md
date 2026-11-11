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

As we know Django server provides the HttpRequest object as a mandatory argument to a view function. We can declare a view with additional parameters that can be fetched from the urlpatterns.

- Example: a `user()` function as a view in the app, with name as a string parameter. the funtion should insert the received string in the Welcome message to be returned as the response.

    - the function needs to be mapped with a URL router `user/` in the app's URL pattern list.
    - the route needs to have a variable part corresponding to the parameter of the view function and must be put inside angular brackets < and > for Django to capture the value and pass to the function. 
        - in this instance the URL route should be `user/<name>/` and mapped with the `views.user` function.

Different types of path parameters can be passed to the function. The parameter inside angular brackets is of `str` type. Some of these types need an appropriate path converter prefix e.g., `<int:userID>`, which lets Django interpret the parameter as an integer.


| Path Converter | Description |
| --- | --- |
| str | Matches any non-empty string |
| int | To read an integer parameter from the URL, we use int: inside the angular brackets e.g., `<int:userID>`. any non-negative integer may be present. |
| slug | A slug is a string that can only include characters, numbers, dashes, and underscores. E.g., `<slug:post:title>`. |
| uuid | This converter matches a formatted UUID. As a convention, to prevent multiple URLs from mapping to the same page, dashes must be included and letters must be lowercase |
| path | This converter matches any non-empty string, including the path separator, `/`, so as to allow us to match against a complete URL path rather than a segment of a URL path as with str. 

**Serving Web Pages**

The view function returns its response in the form of an `HttpResponse` object, with a string a its content. In addition, other HTTP headers may be included in the constructor.

- by default, the `Content_Type` header is `text/html`/. any HTML tags included in the response string are parsed by the browser.
- we cna set it to any other type such as `application/json` if we want to use JSON response [more suitable for APIs].

Instead of passing raw HTML strings, Django allows us to serve an HTML page as the response.

- `render()` function defined in the `django.shortcuts` module is used for the purpose.
- Django can render a static web page as well as a web page with dynamic content which is called a template.

    - to render a web page, the Django server checks if the page is available in any of the directories in the DIRS attribute of the TEMPLATES setting. 
        - we can add templates in the template folder at the root project folder titled BASE_DIR.

`render()` function takes two arguments which are:

- `HttpRequest` object that the view receives from the server.
- contents of the HTML page as the second argument, which is returned as the `HttpResponse`.

The `render()` function can also have a third argument called context - a dictionary object whose values are inserted in the template tags placed inside the HTML code.

## Admine Site

It is a fully customizable, automatic admin interface. Suitable for organisation's internal management use

- the admin app is automatically added to the project as a result of the `startproject` command.
- the admin interface depends on the `django.contrib.admin` app.