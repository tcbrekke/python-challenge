import os
import csv

bank_data = {}
values_list = []
revenue_change = []
date_relabel =[]

pybank_one = os.path.join("PyBank", "budget_data_1.csv")
pybank_two = os.path.join("PyBank", "budget_data_2.csv")
output_txt_file = os.path.join("PyBank", "pybankoutputbd1.txt")

def store_values(input_csv):

	with open(input_csv, "r", newline="") as current_csv:

		csv_reader = csv.reader(current_csv, delimiter=",")
		next(csv_reader)

		for row in csv_reader:
			#Split year from month (assumes year will always come second)
			raw_date = row[0]
			date_relabel = raw_date.split("-")
			#Determine if date is with two or four digit year
			if len(date_relabel[1]) == 2:
				clean_date = str(date_relabel[0]) + " 20" + str(date_relabel[1])
				revenue = int(row[1])
				if clean_date in bank_data:
					bank_data[clean_date].append(revenue)
				else:
					bank_data[clean_date] = [revenue]
			elif len(date_relabel[1]) == 4:
				clean_date = str(date_relabel[0]) + " " + str(date_relabel[1])
				revenue = int(row[1])
				if clean_date in bank_data:
					bank_data[clean_date].append(revenue)
				else:
					bank_data[clean_date] = [revenue]


store_values(pybank_one)

bank_data_combined = {key : sum(values) for key, values in bank_data.items()}

total_revenue = sum(bank_data_combined.values())
months = len(bank_data_combined)

prev_revenue = 0
total_revenue_change = 0
mom_change = 0
max_revenue_change = 0
min_revenue_change = 0

for key, value in bank_data_combined.items():
	current_revenue = value
	current_month = key
	mom_change = current_revenue - prev_revenue
	total_revenue_change = total_revenue_change + mom_change
	if mom_change > max_revenue_change:
		max_revenue_change = mom_change
		month_of_max_change = current_month
	elif mom_change < min_revenue_change:
		min_revenue_change = mom_change
		month_of_min_change = current_month
	prev_revenue = current_revenue
	
avg_revenue_change = total_revenue_change / len(bank_data_combined)

print("Financial Analysis")
print("-----------------------------")
print("Total revenue: $" + str(total_revenue))
print("Total months of data: " + str(len(bank_data_combined)))
print("Average revenue change: $" + str("%0.02f" %(avg_revenue_change)))
print("Greatest monthly increase in revenue: $" + str(max_revenue_change) + " (" + str(month_of_max_change) +")" )
print("Greatest monthly decrease in revenue: $" + str(min_revenue_change) + " (" + str(month_of_min_change) + ")" )

#Print to text file
with open(output_txt_file, "w") as text_file:
	print("Financial Analysis", file=text_file)
	print("-----------------------------", file=text_file)
	print("Total revenue: $" +str(total_revenue), file=text_file)
	print("Total months of data: " + str(len(bank_data_combined)), file=text_file)
	print("Average revenue change: $" + str("%0.02f" %(avg_revenue_change)), file=text_file)
	print("Greatest monthly increase in revenue: $" + str(max_revenue_change), file=text_file)
	print("Greatest monthly decrease in revenue: $" + str(min_revenue_change), file=text_file)
