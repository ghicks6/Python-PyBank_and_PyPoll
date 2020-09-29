# Import Files
import os
import csv

# Path to collect data from the Resources folder
PyPoll_csv = os.path.join('Resources', 'election_data.csv')

# Define the Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open & Read CSV File
with open(PyPoll_csv, newline = '') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read The Header Row First (Skip This Step If There Is No Header)
    csv_header = next(csvfile)

    # Read Each Row of Data After the Header
    for row in csv_reader:

        # Calculate the total number of votes cast
        total_votes += 1

        # Calulate the total number of votes each candidate won
        if (row(2) == "Khan"):
            khan_votes += 1
        elif (row(2) == "Correy"):
            correy_votes += 1
        elif (row(2) == "Li"):
            li_votes += 1
        elif (row(2) == "O'Tooley"):
            otooley_votes += 1

    # Calculate the percentage of votes each candidate won
    khan_percentage = khan_votes / total_votes
    correy_percentage = correy_votes / total_votes
    li_percentage = li_votes / total_votes
    otooley_percentage = otooley_votes / total_votes

    # Calculate the winner of the election
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner = khan_votes
        winner_name = "Khan"
    elif winner = correy_votes
        winner_name = "Correy":
    elif winner = li_votes
        winner_name = "Li"
    elif winner = otooley_votes
        winner_name = "O'Tooley"

# Print the findings to the Terminal
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {khan_percentage.3%}, {khan_votes}")
print(f"Correy {correy_percentage.3%}, {correy_votes}")
print(f"Li:, {li_percentage.3%}, {li_votes}")
print(f"O'Tooley: {otooley_percentage.3%}, {otooley_votes}")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Path to create a Text File with the Output
output_file = os.path.join('Resources', 'output.txt')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

    # Write the Results as a Text File
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"Khan: {khan_percentage.3%}, {khan_votes}\n")
    txtfile.write(f"Correy {correy_percentage.3%}, {correy_votes}\n")
    txtfile.write(f"Li:, {li_percentage.3%}, {li_votes.3%}\n")
    txtfile.write(f"O'Tooley: {otooley_percentage.3%}, {otooley_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")

    