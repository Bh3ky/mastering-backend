# Lesson 1 — Thinking in Objects

**OOP models things**

- a bank account is a thing. it has:
    1.  state (data)

    ```text
    owner = "Brian"
    balance = 500
    ```

    2. behavior (actions)

    ```text
    deposit()
    withdraw()

- in OOP:
    - data + data are bundled together (that bundle is an **object**)
- an object is a real instance created from that blueprint

```text
Class -> BankAccount
Object -> brian_account
```

**Example Code:**

```python
# example class
class BankAccount:
    pass
```

## Creating objects

```python
account1 = BankAccount()
account2 = BankAccount()
```

- here we have two seperate objects.

Note: 

```text
account1 != account2
```

- even though both come from the same class, each object has **its own memory and state**. 

## Adding state with attributes

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
```

**Question: what is the purpose of `__init__`??**
-  `__init__` runs automatically when an object is created

```python
account = BankAccount("Brian", 500)
```

- Python internally does:

```python
__init__(account, "Brian", 500)
```

- i.e.,:

```python
self = account
```

`self` - refers to the current object instance.

- Note: without `self`, Python cannot know which object's data to use.

```text
account1
├── owner = "Brian"
└── balance = 500

account2
├── owner = "Alice"
└── balance = 900
```

## Adding behavior

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

Usage:

```python
account = BankAccount("Brian", 500)
account.deposit(200)

print(account.balance)
```

Note: methods operate on object state

`self.balance += amount` means modify THIS object's balance


# Lesson 2 - Encapsulation & Validation

- from the class we have created we can see that our class allows this:

```python
account.balance = -1000000
```

- this is dangerous. 

objects should protect their own state and this is where **encapsulation** comes in. 

**Question: what is encapsulation??**
- encapsulation means an object controls its own data, (rather than allowing direct unsafe modification). 

file: `app/models/bank_account.py`

```python
class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.amount = amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        
        self._balance -= amount

    def display_balance(self):
        print(f"{self.owner} has ${self._balance}")

    @property
    def balance(self):
        return self._balance
```

`_balance` is a convention i.e.,

> internal attribute — don't modify directly

Question: why not use balance directly??
- because it is dangerous as we might end with invalid objects.

 `@property` allows 

```python
account.balance
```

while internally calling `balance()`

- NB: this creates controlled read-only access. 

# Lesson 3 — Composition & Object Relationships

- composition means an object contains other objects. for example:

```text
BankAccount has a TransactionHistory
Bank has a collection of accounts
Customer has a bank account
```

Note: this is different from inheritance.

Inheritance: `Dog is a animal`

Composition: `Car has a engine`


**Question: why composition matters??**
- it reduces tight coupling, improves flexibility, improves maintainability, and avoids inheritance complexity. 

- by now it should be becoming clear of what we are building:

```text
Bank
├── manages many accounts
│
BankAccount
├── owner
├── balance
├── transaction history
│
Transaction
├── type
├── amount
├── timestamp
```

- now we create a transaction class

file: `app/models/transaction.py`

```python
from datetime import datetime


class Transaction:
    def __init__(self, transaction_type: str, amount: float):
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"{self.transaction_type.upper()} | "
            f"${self.amount} | "
            f"{self.timestamp}"
        )
```

1. Objects can obtain meaningful data
- i.e., a transaction is now its own object instead of just `deposit 200`. here we model it properly. 

2. `datetime.now()` - creates timestamps automatically. 
- every transaction now automatically records type, amount, and creation time. 

3. `__str__` - controls how objects display when printed
- e.g., `print(transaction)`. without `__str__`, Python prints ugly memory addresses. 


- next we need to upgrade our BankAccount file:

file: `app/models/bank_account.py`

```python
from app.models.transaction import Transaction


class BankAccount:
    account_count = 1000

    def __init__(self, owner: str, balance: float):
        BankAccount.account_count += 1

        self.account_number = f"ACC{BankAccount.account_count}"
        self.owner = owner
        self._balance = balance
        self.transaction_count = 0
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self._balance += amount
        self.transaction_count += 1

        transaction = Transaction("deposit", amount)
        self.transactions.append(transaction)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount
        self.transaction_count += 1

        transaction = Transaction("withdrawal", amount)
        self.transactions.append(transaction)

    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)

    def display_balance(self):
        print(
            f"{self.owner} "
            f"({self.account_number}) "
            f"has ${self._balance}"
        )

    def show_transactions(self):
        print(f"\nTransaction History for {self.owner}")

        for transaction in self.transactions:
            print(transaction)
```

`self.transactions = []` - means each bank owns a collection of Transaction objects (_composition_).

```text
BankAccount
│
├── owner
├── balance
└── transactions
     ├── Transaction
     ├── Transaction
     └── Transaction
```

- next we create a high-level system object

file: `app/models/bank.py`

```python
class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def show_all_accounts(self):
        print(f"\nAccounts in {self.name}")

        for account in self.accounts:
            print(
                f"{account.account_number} | "
                f"{account.owner} | "
                f"${account.balance}"
            )
```

- update `main.py`:

```python
from app.models.bank import Bank
from app.models.bank_account import BankAccount


bank = Bank("Python National Bank")

account1 = BankAccount("Brian", 1000)
account2 = BankAccount("Alice", 500)

bank.add_account(account1)
bank.add_account(account2)

account1.deposit(300)
account1.withdraw(150)

account1.transfer(account2, 200)

account1.display_balance()
account2.display_balance()

account1.show_transactions()

bank.show_all_accounts()

```


# Lesson 4 - Inheritance & Method Overiding

- inheritance allows one class to reuse another class.

Example:

```text
SavingsAccount IS-A BankAccount
```

- a savings account already has:
    - owner, balance, deposit(), withdraw(), transactions
- we do not rewrite them, instead we inherit them

- NB: without inheritance we would have duplication

1. we'll need to refactor base class

file: `app/models/bank_account.py`

```python
from app.models.transaction import Transaction


class BankAccount:
    account_count = 1000

    def __init__(self, owner: str, balance: float):
        BankAccount.account_count += 1

        self.account_number = f"ACC{BankAccount.account_count}"
        self.owner = owner
        self._balance = balance
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        self._validate_amount(amount)

        self._balance += amount

        self._add_transaction("deposit", amount)

    def withdraw(self, amount: float):
        self._validate_amount(amount)

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount

        self._add_transaction("withdrawal", amount)

    def transfer(self, target_account, amount: float):
        self.withdraw(amount)
        target_account.deposit(amount)

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

    def _add_transaction(self, transaction_type, amount):
        transaction = Transaction(transaction_type, amount)
        self.transactions.append(transaction)

    def show_transactions(self):
        print(f"\nTransactions for {self.owner}")

        for transaction in self.transactions:
            print(transaction)

    def __str__(self):
        return (
            f"{self.account_number} | "
            f"{self.owner} | "
            f"Balance: ${self.balance}"
        )
```

- here we can see `_validate_amount()` and `_add_transaction`: these are reusable internal helper methods.
    - NB: the underscore means internal implementation only. not intended for external use. 

2. next, we create a SavingsAccount file

file: `app/models/savings_account.py`

```python
from app.models.bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(
        self,
        owner: str,
        balance: float,
        interest_rate: float
    ):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)

        self._balance += interest

        self._add_transaction("interest", interest)
```

- `super()` here calls the parent constructor i.e., initialise everything from BankAccount first.
    - without it, owner, balance, and transaction wouldn't exist.
- allows SavingsAccount to receive `deposit()`, `withdraw()`, `transfer()`, and `show_transactions()` automatically. 

3. create CurrentAccount file to allow overdraft

file: `app/models/current_account.py`

```python
from app.models.bank_account import BankAccount


class CurrentAccount(BankAccount):
    def __init__(
        self,
        owner: str,
        balance: float,
        overdraft_limit: float
    ):
        super().__init__(owner, balance)

        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        self._validate_amount(amount)

        allowed_amount = (
            self.balance + self.overdraft_limit
        )

        if amount > allowed_amount:
            raise ValueError(
                "Overdraft limit exceeded."
            )

        self._balance -= amount

        self._add_transaction(
            "current account withdrawal",
            amount
        )
```

- here we experience method overiding. the parent class already had `withdraw()` but CurrentAccount replaces it with specialised behavior.

- all accounts expose `withdraw()`, but savings account behave one way and current accounts behave another way. this is referred to as **Polymorphism** in Python. 

4. we create BusinessAccount file for business accounts to charge withdrawal fees.

file: `app/models/business_account.py`

```python
from app.models.bank_account import BankAccount


class BusinessAccount(BankAccount):
    WITHDRAWAL_FEE = 5

    def withdraw(self, amount: float):
        total_amount = amount + self.WITHDRAWAL_FEE

        super().withdraw(total_amount)

        self._add_transaction(
            "withdrawal fee",
            self.WITHDRAWAL_FEE
        )
```

- NOTE: `super().withdraw(total_amount)` here we the parent's withdrawal logic. we reuse:
    - validation, insufficient funds logic, and transaction handling itself without having to rewrite everything.

5. update `main.py`

```python
from app.models.savings_account import SavingsAccount
from app.models.current_account import CurrentAccount
from app.models.business_account import BusinessAccount


savings = SavingsAccount(
    "Brian",
    1000,
    5
)

current = CurrentAccount(
    "Alice",
    500,
    1000
)

business = BusinessAccount(
    "Tech Corp",
    10000
)

savings.apply_interest()

current.withdraw(1200)

business.withdraw(1000)

print(savings)
print(current)
print(business)

savings.show_transactions()
current.show_transactions()
business.show_transactions()
```


