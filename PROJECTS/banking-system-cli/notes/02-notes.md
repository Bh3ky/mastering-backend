## CLI Authentication System

- now we are working on the **domain layer**.

```text
Bank
 ├── Customer
 │     └── Account(s)
 │
 └── Authentication
```

- transforming `account.deposit(500)` into:

```text
====================================
          PYBANK CLI
====================================

1. Create Account
2. Login
3. Exit

Select option:
```

- Note: the user should never interact with objects directly. instead:

```text
User
 ↓
CLI
 ↓
Bank Service
 ↓
Domain Models
```


**Why introduce a Service Layer??**

- right now:

```python
bank.create_customer(...)
bank.create_account(...)
```

- works. but if we are to add validation, database writes, logging, notifications, fraud checks etc we wouldn't want the CLI code talking directly to models. instead:

```text
CLI
 ↓
BankingService
 ↓
Bank
```

**Session Concept**

- when a login succeeds:

```python
logged_in_account = account
```

- that variable becomes the current session. this is very similar to web sessions, JWT authentication, or API token. this is referred to as **state management**.


- now we need to introduce dedicated validation layer:

```python
validate_pin()
validate_amount()
validate_name()
```

- and other custom exceptions