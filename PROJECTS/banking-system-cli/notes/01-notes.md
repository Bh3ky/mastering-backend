## Core Domain Model

- first we need to create reusable generators

file: `app/utils/generators.py`

- create customer model

Note: `self.accounts = []` is an example of composition which is a common systems design technique. here the relationship is one customer can have multiple accounts

```text
Customer
│
├── Account #1
├── Account #2
└── Account #3
```

- in database later:

```text
customers
    |
    | 1 : many
    |
accounts
```

- the same model will transfer directly into SQL.


- the method `_record_transaction()` has a leading underscore meaning that it's internal/private and other classes should not call it directly. only `deposit()` and `withdraw()` can use it. _encapsulation_


- now that accounts exist, we can link them for example:

```python
customer = Customer(
    "Brian",
    "Doe"
)

account = BankAccount(
    owner=customer,
    pin="1234"
)

customer.add_account(account)
```

relationship:

```text
Customer
    |
    +-- Account
```

## Authentication

- right now our objects exist independently:

```python
customer = Customer(...)
account = BankAccount(...)
```

- but who manages them? who creates accounts? who searches accounts? who authenticates users? who ensures account numbers are unique?
- this is the responsibility of the Bank.

**What is an Aggregate Root?**

In Domain-Driven Design (DDD), an aggregate root is the main object responsible for managing a group of related objects. 

- for our system:

```text
Bank
│
├── Customers
│
├── Accounts
│
└── Authentication
```

- everything flows through the Bank.
- instead of `account = BankAccount(...)` we have `bank.create_account(...)`. this gives us a single control point. 


**Why Dictionaries??**

- we use `self.accounts = {}` instead of `self.accounts = []` why??
    - a list would require a for loop: 
    ```python
    for account in accounts:
        ...
    ```
    - every time we search which leads to a complexity of O(n).

    - on the other hand a dictionary gives `accounts[account_number]` with a complexity of O(1).
