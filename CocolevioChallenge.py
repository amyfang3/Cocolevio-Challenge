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
# Time Complexity: O(n^3)
# Space Complexity: O(n)

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

2. Sort remaining companies by profit
3. Fill up until no material left

"""
def function(list_all_companies, total_amount_material):
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

def mergeSort(alist):

    print("Sorting ", alist)
    dummy = input("")

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        print("Recursive call on left half")
        mergeSort(lefthalf)
        print("Recursive call on right half")
        mergeSort(righthalf)

        i = 0  # index of left list
        j = 0  # index of the right list
        k = 0  # index of overall list (passed in as an argument)

        print("merging", lefthalf, "and", righthalf)
        dummy = input("")
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
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

        print("result of merge:", alist)
        dummy = input("")



