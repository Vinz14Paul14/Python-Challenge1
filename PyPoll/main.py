import os
import csv

#variables
total_votes = 0
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0

#need help opening the correct csv file?
election_data = os.path.join("Resources", "election_data.csv")


with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    for row in election_data:

    candidate1 = {"name" : "Khan",
                "total_votes" : 2218231"}
    candidate2 = {"name" : "Correy",
                "total_votes" : 704200"}
    candidate3 = {"name" : "Li",
                "total_votes" : 492940"}
    candidate4 = {"name" : "O'Tooley",
                "total_votes" : 105630"}

        total_votes = total_votes + 1

        if (row[2] == "candidate1"):
            candidate1_votes = candidate1_votes + 1
        elif (row[2] == "candidate2"):
            candidate2_votes = candidate2_votes + 1
        elif (row[2] == "candidate3"):
            candidate3_votes = candidate3_votes + 1
        else:
            candidate4_votes += 1

    khan_percent = candidate1_votes / total_votes
    correy_percent = candidate2_votes / total_votes
    li_percent = candidate3_votes / total_votes
    otooley_percent = candidate4_votes / total_votes

    winner = max(candidate1_votes, candidate2_votes, candidate3_votes, candidate4_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
         winner_name = "O'Tooley"

print(f"Election Results")
print(f"---------------------")

