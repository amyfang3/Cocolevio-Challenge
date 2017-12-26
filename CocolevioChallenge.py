import itertools

# stores a company's info
class Company():

	def __init__(self, name, amount, price):
		self.name = name
		self.amount = amount
		self.price = price
		self.profit = amount * price

	def __str__(self):
		string = "Company" + self.name
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


#--------------------------------------------------------------
# Brute Force Solution

# finds all possible permutations of companies
def findAllCombos(list_all_companies):
	all_combos = []
	for size in range(1, len(list_all_companies) + 1):
		combos = itertools.combinations(list_all_companies, size) #runtime: O(n^2)
		for combo in combos:
			all_combos.append(combo)

	return all_combos

# calculates the highest profit and returns a list of company names
def maxProfit(total_amount_material, list_all_companies):
	all_combos = findAllCombos(list_all_companies)
	max_combo = 0
	max_profit = 0

	# checks each combo
	for combo in all_combos:
		total_amount = 0
		total_profit = 0

		# adds total amount and total profit
		for company in combo:
			total_amount += company.amount
			total_profit += company.profit

		# if total amount exceeds total amount materials, combo is disqualified
		if total_amount > total_amount_material:
			continue
		
		# if combo's profit is more than max profi so far, replace max combo and max profit
		if total_profit > max_profit:
			max_profit = total_profit
			max_combo = combo

	return max_combo




def main():
	list_all_companies = upload()
	total_amount_material = eval(input("How much material is there? "))
	combo = maxProfit(total_amount_material, list_all_companies)
	for x in combo:
		print(x)

main()

#--------------------------------------------------------------

"""
Approach 2: Better Runtime

1. Eliminate all companies that go over the total amount of mateiral
   Return list of leftover companies

2. Go through remaining combinations, stopping a branch when it goes over

A --> AB --> ABC (disqualified)
  --> AC --> ACD --> ACDE
         --> ACE (disqualified)
  --> AD --> ADE

"""



