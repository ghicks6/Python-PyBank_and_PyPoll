# Import Files
import os
import csv

# Path to collect data from the Resources folder
PyBank_csv = os.path.join('Resources', 'budget_data.csv')

 # Define the Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Open & Read CSV File
with open(PyBank_csv, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")


    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csv_reader)
    row = next(csv_reader)

    #  Set variables for Total Months, Net Amount of Profit/Loss, & Greatest Increase/Greatest Decrease
    previous_profit = int(row[1])
    total_months = total_months + 1
    net_amount = net_amount + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    greatest_decrease = int(row[1])
    greatest_decrease_month = row[0]

    # Move through each row in dataset:
    for row in csv_reader:

        # Calculate the total number of months
        total_months = total_months + 1

        # Calculate the net proft/loss
        net_amount = net_amount + int(row[1])

        # Calculate the change from previous month to this month
        change = int(row[1]) - previous_profit
        monthly_change.append(change)
        previous_profit = int(row[1])
        month_count.append(row[0])

        # Calculate the greatest increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Calculate the greatest decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
            

    # Calculate the average change
    average_change = sum(monthly_change)/len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis to the Terminal
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total Profit/Loss: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# Path to create a Text File with the Output
output_file = os.path.join('Resources', 'output.txt')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

    # Write the Data as a Text File
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total Profit/Loss: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
