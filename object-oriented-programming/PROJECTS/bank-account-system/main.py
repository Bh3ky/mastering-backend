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