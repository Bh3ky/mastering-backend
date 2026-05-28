# OOP Concepts

**Question: what is Object-Oriented Programming??**
- it is a way of organising code that uses objects and classes to represent real-world entities and behavior.

OR
- programming paradigm that organises software design around objects—data structure that contain both data (attributes) and behavior(methods). allows us to model real-world entities like a car, a bank account, a user etc.

- in OOP, object has attributes thing that has a specific data and can perform certain actions using methods. 
    - organise code into classes and objects
    - support encapsulation to group data and methods together
    - enables inheritance for reusability and hierarchy
    - allows polymorphism for flexible method implementation


## Class
- a class is a collection of objects. classes are blueprints for creating objects.

**Question: what is a class??**
- a class defines a set of attributes and methods that the created objects (instances) can have. 

- classes are created by keyword class.
- **attributes are the variables** that belong to a class.
    - they are always public and can be accessed using the dot (.) operator e.g., `Myclass.Myattribute`


**Question: how do we create a class??**

```python
class Dog:
    species = "Canine" # class attribute

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute
```

- here, we used `class Dog` to create a class named Dog, which acts as a blueprint for dog objects.
    - species is a class attribute i.e., it is shared by all instances of the class.
    - `__init__()` - constructor method that runs automatically when a new object ia created. used to initialise object data.
    - `self` refers to the current object, allowing each object to store and access its own data.
    - self.name and self.age are instance attributes, unique to each Dog object created from the class.


**Question: what are objects??**
- an object is an instance of a class. it represents a specific implementation of the class and holds its own data.
- an object consists of:
    - state - represented by the attributes and reflects the properties of an object
    - behavoir - represented by the methods of an object and reflects the response of an object to other objects. 
    - identity - gives a unique name to an object and enables one object to interact with other objects. 


**Question: how do we create an object??**
- creating an object involves instantiating a class to create a new instance of that class. the process is also referred to as object instantiation.

```python
class Dog:
    species = "Canine" # class attribute

    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age  # instance attribute

# creating an object of the Dog class
dog1 = Dog("Buddy", 3)
print(dog1.name) # accesses the instance attribute name of the dog1 object
print(dog1.species) # accesses the class attribute species of the dog1 object
```


## Four Pillars of OOP
- these form the foundation for designing structured, reusable, and maintainanle software

**1. Inheritance**
- inheritance allows a class (child class) to acquire properties and methods of another class (parent class). 
- promotes code reuse. 

**2. Polymorphism**
- polymorphism means "same operation, different behavior".
- allows functions or methods with the same name to work differently depending on the type of object they are acting upon. 

Types of polymorphism
- compile-time polymorphism (mimicked using *args & **kwargs) - method overloading
- runtime polymorphism  - method overriding, duck typing, and operator overloading

**3. Encapsulation**
- encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions. 
- a class is an example of encapsulation as it groups together member functions, variables and other related data in a single unit. 

**4. Data Abstraction**
- abstraction hides the internal implementation details while exposing only the necessary functionality. 
- helps focus on "what to do" rather than "how to do it".
