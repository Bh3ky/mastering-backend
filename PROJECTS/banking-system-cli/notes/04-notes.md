## Persistence (JSON Storage)

- up until now, our bank has only been existing in memory. now we need to persist the data to the disk. 

**System Design Perspective**

- introducing a new layer:

```text
CLI
 ↓
Service
 ↓
Domain
 ↓
Storage
```

- something to note, the data won't be accessed using `with open("accounts.json") as file:` inside our models. NO NO NO
- NB: models shouldn't know where data is stored.


- there is a problem that needs to be solved. Python objects cannot be stored directly.
- this fails: `json.dump(account)` because BankAccount is not JSON serializable.
- thus, every domain model needs `to_dict` and eventually `from_dict`.


- on the previous lesson, we were able to convert `Customer(...)` into:

```json
{
    "customer_id": "...",
    "first_name": "...",
    "last_name": "..."
}
```
- now we have to do the reverse. why??? when the application starts `service = BankingService()` we want:

```text
Load JSON
↓
Rebuild Customers
↓
Rebuild Accounts
↓
Restore Relationships
↓
Application Ready
```