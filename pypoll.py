import os
import csv

votes_per_candidate = {}
total_votes_cast = 0 

pypoll_one = os.path.join("PyPoll", "election_data_1.csv")
pypoll_two = os.path.join("PyPoll", "election_data_2.csv")
#pypoll_combined = os.path.join("PyPoll", "election_data_clean.csv")
output_txt_file = os.path.join("PyPoll", "pypolloutput.txt")


def store_values(input_csv):

	with open(input_csv, "r", newline="") as current_csv:

		csv_reader = csv.reader(current_csv, delimiter=",")
		next(csv_reader)

		for row in csv_reader:
			candidate = row[2]
			if candidate in votes_per_candidate:
				votes_per_candidate[candidate].append([1])
			else:
				votes_per_candidate[candidate] = [1]


store_values(pypoll_one)
store_values(pypoll_two)

vpc_combined = {key : len(values) for key, values in votes_per_candidate.items()}
total_votes = sum(vpc_combined.values())

print("Election Results")
print("--------------------")
print("Total votes: " + str(total_votes))
print("--------------------")
for key, value in vpc_combined.items():
	print(key + ": " + str("{:.2%}".format(value / total_votes)) + " (" + str(value) + " votes)")
	winner = max(vpc_combined, key=lambda key: vpc_combined[key])
print("--------------------")
print("Winner: " + str(winner))

with open(output_txt_file, "w") as text_file:
	print("Election Results", file=text_file)
	print("--------------------", file=text_file)
	print("Total votes: " + str(total_votes), file=text_file)
	print("--------------------", file=text_file)
	for key, value in vpc_combined.items():
		print(key + ": " + str("{:.2%}".format(value / total_votes)) + " (" + str(value) + " votes)", file=text_file)
		winner = max(vpc_combined, key=lambda key: vpc_combined[key])
	print("--------------------", file=text_file)
	print("Winner: " + str(winner), file=text_file)
