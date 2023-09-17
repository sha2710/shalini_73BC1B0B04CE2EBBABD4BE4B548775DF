Challenge 2:

Programe:1


class Bank:
	def _init_(self):
		self.total_amount = 0
		self.name = ''

	def welcome(self):
		self.name = input('Welcome to your Bank Account. Please Enter your name: ')

	def print_current_balance(self):
		print('Your Current balance : {}'.format(self.total_amount))

	def deposit(self):
		self.total_amount += float(input('Hello {}, please enter amount to deposit: '.format(self.name)))
		self.print_current_balance()

	def withdraw(self):
		amount_to_withdraw = float(input('Enter amount to withdraw: '))

		if amount_to_withdraw > self.total_amount:
			print('Insufficient Balance !!')
		else:
			self.total_amount -= amount_to_withdraw

		self.print_current_balance()


if _name_=="__main__":
	bank = Bank()
	bank.welcome()

	while Tru…