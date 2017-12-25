class Company():

	def __init__(self, name, amount, price):
		self.name = name
		self.amount = amount
		self.price = price

	def __str__(self):
		string = "Company " + self.name
		string += "\nAmount: " + self.amount
		string += "\nPrice: " + self.price
		return string

# consolidating data about companies into a list of objects from a csv file
def upload(datafile):
	with open("datafile.csv", "r") as f:
		data = f.readlines()

	for i in range(len(data)):
		data[i] = data[i].split(',')
		data[i][-1] = data[i][-1].replace("\n", "")

	num_of_companies = len(data[i]) - 1
	list_all_companies = []

	# data[0] = name
	# data[1] = amount
	# data[2] = price

	# adds each company to the list
	for i in range(num_of_companies):
		list_all_companies.append(Company(data[0][i+1], data[1][i+1], data[2][i+1]))

	return list_all_companies










def function(totalAmountMaterial, data):