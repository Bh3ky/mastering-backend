from app.models.bank import Bank
from app.models.bank_account import BankAccount

bank = Bank("XL Bank")

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