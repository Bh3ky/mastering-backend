# Testing the REST API

- testing is a process of checking whether the actual software product performs as expected and is bug free.
    - aim: detect failures, including bugs and performance issues in the application.  

What is software testing?

- Software testing is the process of examining the behavior of the software under test for validation or verification.
- considers the attributes of reliabiity, scalability, reusability, and usability to evaluate the execution of the software components (servers, database, application, and so on) and find software bugs, errors, or defects.

Testing is typically classified into three categories:

- functional testing - this type of testing comprises unit, integration, user acceptance, globalization, internationalization testing etc
- non-functional testing - checks for factors such as performance, volume, scalability, usability, and load
- maintenance testing - considers regression and maintainance

## Understanding manual testing

- manual testing is the process of testing software manually to find defects or bugs. It’s the process of testing the functionalities of an application without the help of automation tools.

## Understanding automated testing

- automated testing is simply the process of testing software using automation tools to find defects. automations tools can be scripts written in the language used to buils the application or some software or drivers such as Selenium, WinRunner, and LoadRunner.

## Testing in Django

- Pytest is used, which is a framework for writing small and readable tests. in API testing is used to write code to test API endpoints, databases, and UI.

**Testing pyramid**

![testing pyramid](image-4.png)

1. unit tests - target individual components or functionality to check whether they work as expected in isolated conditions. 
2. integration tests - test how code interacts with other code or other parts of the software. can also be a test between the application and an external service e.g., payment API.
3. end-to-end tests - ensure that the software is working as required. test how the application works from beginning to end.

**Test-Driven-Design (TDD)**

- software development practices that focus on writing unit test cases before developing the feature.
    - ensures optimized code, application of design patterns and better architecture, helps developers understand the business requirements, and makes the code flexible and easier to maintain.

## Writing tests for Django models

- alwways a good idea to start writing tests for the models in a Django project.
    - helps to make sure that methods or attributes on the model are well represented in the database.

## Writing tests for the User model

- add a new file `tests.py` inside the `core/user` directory

What is a decorator?

- it a funtion which takes another function as its argument and returns another function. `@pytest.mark.django_db` gives us access to the Django database.

## Writing tests for the Post model

- to create a model, we need to have a user object ready. this will also be the same for the `Comment` model. to avoid repetition, we will simply write fixtures.

What is a fixture?

- it is a function that will run before each test function to which it is applied. here, the fixture will be used to feed some data to the tests.

- create `fixtures/` in the `core/` directory. then inside the `core/post/` directory inside the `tests.py` file we then test the creation of a post.

## Writing tests for the Comment model

- create a new file `post.py` inside the `core/fixtures` directory.
- this file contains the fixture of a post which is needed to create a comment. Pytest allows us to inject fixtures into other fixtures. in this instance, the `post` fixture needs a `user` fixture.

- then we write the test for comment creation inside the `core/comment` directory.

## Writing tests for Django viewsets

- viewsets or endpoints are the interfaces of the business logic that the external clients will use to fetch data and create, modify, or delete data. 

- great habit to have tests to make sure that the whole system, starting from a request to the database, is working as intended.

- first, we need to configure the Pytest environment to use the API client from DRF.
    - API client is a class that handles different HTTP methods, as well as features such as authentication in testing, which can be very helpful for direct authentication without a username and password to test some endpoints. 

- we create a file `conftest.py` at the root of the project.

## Writing tests for authentication

- create a file `tests.py` inside the `core/auth` directory. here instead of writing test functions directly, we write a class that will contain the testing methods.

- NB: within the `test_refresh` method, we log in to get a refresh token to make a request to get a new access token.

## Writing tests for PostViewSet

- follow the DRY rule.

- `PostViewSet` handles requests for two types of users:
    - authenticated users
    - anonymous users

- each type of user has different permissions on the `post` resource.
