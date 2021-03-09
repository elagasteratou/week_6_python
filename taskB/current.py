from account import Account

class Current(Account):
    # available_including_overdraft and initial was missing from the parameters on line 5.
    def __init__(self, initial, available_including_overdraft):
        self.__available_including_overdraft = available_including_overdraft
        super().__init__(initial)


    # we need to clarify what we are showing here and the calculations
    # def display_overdraft(self):
    #     return self.__available_including_overdraftoverdraft = self + 1000

