from account import Account
from current import Current

mg_account = Account(1000)
cd_account = Account(700)

cd_account.deposit(40)
mg_account.deposit(20)

cd_account.withdraw(1500)
# cd_account.getbalance is a method and needs round brackets at the end. and the required parameters passed to it.
print(cd_account.getbalance())
print(mg_account.getbalance())


# we have to make sure we are passing the parameters we said we will have when creating the functions/methods
cd_current_account = Current(cd_account, 0)
print("total including over draft on CD account is:", cd_current_account.display_overdraft())

# print(cd_account.display_overdraft())


