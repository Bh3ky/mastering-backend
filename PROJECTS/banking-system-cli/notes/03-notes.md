## Validation, Custom Exceptions, and Input Sanitization

- our goal now is to prevent invalid data from entering the syste. right now these are possible:

```text
First name: 12345
PIN: banana
Deposit: -500
Withdraw: -100
```

- first we need to create our custom exceptions to replace the current one `raise ValueError("Insufficient funds")`. why??? every failure is the same `ValueError` we cannot distinguish:

```text
Invalid PIN
Insufficient Funds
Negative Deposit
Account Locked
```
