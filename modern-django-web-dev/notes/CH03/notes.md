# Chapter 03 - Django ORM

Large, complex, and dynamic web-based applications are always data driven. The application invariably uses a certain database backend for data storage and retrieval. 

Instead of interacting with the database with raw SQL queries, Django recommends handling the database through an abstraction layer having Python objects callec **models**. 

**Objectives**

- [] DB-API
- [] ORM
- [] Database configuration
- [] Model class
- [] Migrations
- [] Django admin shell
- [] CRUD operations
- [] Model field types
- [] Model relationships

## DB-API

The Python Database API (DB-API) is a collection of specifications recommended to be implemented by the database access modules for any relational database.

- Python modules acting as interface for respecrive relational databases - such as `mysqldb` or `mysqlclient` for MySQL, `psycopg` for PostgreSQL - use the same set of classes, objects, and functions as defined in the DB-API.

**SQLite** - it is a lightweight, file-based, serverless database.

- Python's standard library readily provides built-in support for working with SQLite in the form of sqlite3 module.
- to interact with a database, the first step is to establish a connection and obtain a connection object.

```python
import sqlite3
conn=sqlite3.connect("mydata.sqlite3")
```

- then we obtain a cursor object that acts as a handle to the database. this cursor object is responsible for executing all the SQL queries that perform `CREATE`, `RETRIEVE`, `UPDATE`, and `DELETE` operations which are known as **CRUD operations**.

```python
cur = conn.cursor()
```

- now we can call the `execute()` method of the cursor object and pass a string representing a valid SQL query to it.

Example: Create a Books table with field structure in the `mydata.sqlite3` database

```python
import sqlite3

conn = sqlite3.connect("mydata.sqlite3")
cur = conn.cursor()

qry='''
CREATE TABLE IF NOT EXISTS Books (
    id INTEGER (10) PRIMARY KEY,
    title STRING (50),
    author STRING (20),
    price INTEGER (10),
    publisher STRING (20)
    );
'''

cur.execute(qry)
conn.close()
```

The database can be accessed in a Django view function. How?? We pass a `SELECT` query to the execute() method of the cursor object from the sqlite3 module.

We can also use another view function to fetch a specific record whosw `id` is captured from the URL route as a path parameter.

- the `book()` view function takes two arguments; first one being the request object and the second one is id, which Django provides by parsing the mapped URL route.
- the SQL query is prepared statement that substitutes the value of id receieved from the URL dispatcher in the `SELECT` statement.

    - NOTE: the record returned by the `fetchone()` method of the cursor is rendered as the responnse.