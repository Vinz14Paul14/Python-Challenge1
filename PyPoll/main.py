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
    vote_count = {}

    for abc in csvreader:
        if abc[2] not in candidate_names: 
            candidate_names.append(abc[2])
            vote_count[abc[2]] = 1
        vote_count[abc[2]] = vote_count[abc[2]] + 1
        total_votes = total_votes + 1

    print(total_votes)
    print(candidate_names)
    print(vote_count)

    winner = ""
    max_votes = 0
    for abc in vote_count:
        votes = vote_count.get(abc)
        if votes > max_votes :
            max_votes = votes
            winner = abc 
        print(abc,votes)
        total_percentage = float((votes / total_votes) * 100)
        print(total_percentage)
        print(f"{total_percentage:.2f}%")
        print("The Winner is " + winner + " "+ str(max_votes))

