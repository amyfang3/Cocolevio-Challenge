import itertools

"""
Solution
1. Eliminate all companies that go over the total amount of mateiral
   Return list of leftover companies

2. Sort remaining companies by profit
3. Add companies until no material left

Time complexity: O(n log n)
"""

# class to store a company's info
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


def maxProfit(list_all_companies, total_amount_material):
	new_list = []
	total_requested_amount = 0

	# eliminates all individual companies that go over total amount
	for company in list_all_companies:
		total_requested_amount += company.amount
		if company.amount <= total_amount_material:
			new_list.append(company)

	# if there is not enough material for any individual company
	if new_list == []:
		return "Not enough material to satisfy any company's order"
	# if total amount fulfills only one company's order
	elif len(new_list) == 1:
		return new_list[0]
	# if total amount fulfills all orders
	elif total_requested_amount <= total_amount_material:
		return list_all_companies
	else:
		# find a combination of companies to maximize profit
		# sort remaining companies by profit
		mergeSort(new_list)
		new_list.reverse()

		# add companies based off of available materials and most profit
		final_list = []
		for company in new_list:
			if company.amount <= total_amount_material:
				final_list.append(company)
				total_amount_material -= company.amount

		return final_list
		
def mergeSort(alist):

	if len(alist) > 1:
		mid = len(alist) // 2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0  # index of left list
		j = 0  # index of the right list
		k = 0  # index of overall list (passed in as an argument)

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i].profit < righthalf[j].profit:
				alist[k] = lefthalf[i]
				i += 1
			else:
				alist[k] = righthalf[j]
				j += 1
			k += 1

		while i < len(lefthalf): # picks up the leftover of the left half if any
			alist[k] = lefthalf[i]
			i += 1
			k += 1

		while j < len(righthalf): # picks up leftovers of the right half if any
			alist[k] = righthalf[j]
			j += 1
			k += 1


def main():
	list_all_companies = upload() # uploads data into program
	total_amount_material = eval(input("How much material is there? "))
	while total_amount_material < 0:
		print("Invalid input. Please try again.")
		total_amount_material = eval(input("How much material is there? "))

	combo = maxProfit(list_all_companies, total_amount_material) # returns list of companies to obtain max profit
	if isinstance(combo, str):
		print(combo)
	else:
		print("These are the companies for maximum profit:")
		for x in combo: print(x)

main()
