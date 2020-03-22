import os
import csv

#variables
total_votes = 0

#need help opening the correct csv file?
election_data = os.path.join("Resources", "election_data.csv")


with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")
    print(csv_header)
    
    candidate_names = []

    for abc in csvreader:
        if abc[2] not in candidate_names: 
            candidate_names.append(abc[2])

        total_votes = total_votes + 1

    print(total_votes)
    print(candidate_names)

