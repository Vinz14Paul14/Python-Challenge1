import os
import csv

#need help opening the correct csv file?
budget_data = os.path.join("Resources", "budget_data copy.csv")

#list to store
profitList = []
changeList = []
averageChange = []
dateList = []

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    count = 0

#read each row
    for row in csvreader:
        profitList.append(row[1])
        dateList.append(row[0])
        count+=1
        if count == 1:
            previous = float(row[1])
        elif count > 1:
            change = float(row[1]) - previous
            changeList.append(change)
            previous = float(row[1])

total_change = sum(changeList)
averageChange = (total_change/ (count - 1))
greatest_increase = max(changeList)
greatest_decrease = min(changeList)

print(f"Summary Title: Financial Analysis")
print("--------------------------------")
print("Total Months: 86")
print(f"Average Change: {str(averageChange)}")
print(f"Greatest Increase in Profits: {str(greatest_increase)}")
print(f"Greatest Decrease in Profits: {str(greatest_decrease)}")

output_file = os.path.join("Resources", "budget_data copy.text")
with open(output_file, "w",) as txtfile:
    txtfile.write(f"Summary Title: Financial Analysis\n")
    txtfile.write(f"--------------------------------\n")
    txtfile.write(f"Total Months: 86\n")
    txtfile.write(f"Average Change: {str(averageChange)}\n")
    txtfile.write(f"Greatest Increase in Profits: {str(greatest_increase)}\n")
    txtfile.write(f"Greatest Decrease in Profits: {str(greatest_decrease)}\n")

    
#export to text file
#python /path/to/script/main.py > /path/to/output/main.txt