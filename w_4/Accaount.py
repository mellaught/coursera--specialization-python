class Value:

	def __init__(self):
		self.money = None 

	def __get__(self, instance, owner):
		return self.money - instance.commission*self.money

	def __set__(self, instance, money):
	    self.money = money


class Account:

    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
	new_account = Account(0.2)
	new_account.amount = 100

	print(new_account.amount)#90
	