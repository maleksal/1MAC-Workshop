class Atm():

	def __init__(self,Bank_name,Balance):
		self.name = Bank_name
		self.balance = Balance
		self.transaction_history = []

	def requestP(self,request):
		self.request = request 
		if self.request > self.balance :
			print ("Your Bank balance is {0}$".format(self.balance))
			print ("We cant afford your request.")
		if self.request <= 0:
			print "More than zero plz!\n\tYou requested {0}$".format(self.request)
		else:
			print ("Welcom to {0} \n\t ---> you requested {1}$".format(self.name,self.request))
			#processing request 
			self.transaction_history.append(request)
			self.do_request(request)
		self.balance -= self.request 	

	@staticmethod 
	def do_request(r):
		papers = [100,50,10,5]
		while r >0 :
			for i in papers:
				while r > i:
					print ("give {0}$".format(i))
					r -= i
			if r != 0:
		   		print ("give {0}$".format(r))
		   		r -= r	


	def transaction(self):
		for i in self.transaction_history:
			print ("\t-->you requested {0}$".format(i))

	def currentbalance(self):
		#balance = self.balance - self.request
		print("Your current balance is {0}$".format(self.balance))

balance = 7000			
bank = Atm("Smart Bank",balance)
bank.requestP(800)
bank.requestP(500)
bank.transaction()
bank.currentbalance()
