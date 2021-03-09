from account import Account
from current import Current

mg_account = Account(1000)
cd_account = Account(700)

cd_account.deposit(40)
mg_account.deposit(20)

cd_account.withdraw(1500)

print(cd_account.getbalance)

cd_account = Current()

print(cd_account.display_overdraft())


