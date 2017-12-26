import itertools

# stores a company's info
class Company():

	def __init__(self, name, amount, price):
		self.name = name
		self.amount = amount
		self.price = price
		self.profit = amount * price

	def __str__(self):
		string = "Company " + self.name
		return string

# consolidating data about companies into a list of objects from a csv file
def upload():
	with open("datafile.csv", "r") as f:
		data = f.readlines()

	# converts each row of data into a list
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
		list_all_companies.append(Company(data[0][i+1], int(data[1][i+1]), int(data[2][i+1])))

	return list_all_companies

# finds all possible permutations of companies
def findAllCombos(list_all_companies):
	all_combos = []
	for size in range(1, len(list_all_companies) + 1):
		combos = itertools.combinations(list_all_companies, size)
		for combo in combos:
			all_combos.append(combo)

	return all_combos

# calculates the highest profit and returns a list of company names
def maxProfit(total_amount_material, list_all_companiesl):
	all_combos = findAllCombos(list_all_companies)
	max_combo = 0
	max_profit = 0

	for combo in combos:
		total_amount = 0
		total_profit = 0

		for company in combo:
			total_amount += company.amount
			total_profit += company.profit

		if total_amount > total_amount_material:
			pass
		
		if total_profit > max_profit:
			max_profit = total_profit
			max_combo = combo

	return max_combo




def main():
	list_all_companies = upload()
	totalAmountMaterial = eval(input("How much material is there? "))
	print(findAllCombos(list_all_companies))
	#print(maximizeProfits(totalAmountMaterial, list_all_companies))

main()


