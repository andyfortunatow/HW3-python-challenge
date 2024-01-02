import csv
import os

csvpath = os.path.join("/Users/drew/HW3-python-challenge/PyPoll/Resources/election_data.csv")

# Creating either counts or empty lists for the following variables
total_vote = 0
candidate_votes = {}
candidate_list = []
votes_count = []
percentage_voted_list = []
winner = ""
winner_votes_count = 0
cleaned_output = []

# Open CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") 

  # Skip first row
    header = next(csvreader)

    # Loop through rows
    for row in csvreader:

        # Counting total number of votes (excluding row 1)
        total_vote = total_vote + 1
        
        # Defining Row 2 as the candidate name
        candidate_name = row[2]
        
        # If candidate name is already in the list, then add one to the vote count
        if candidate_name in candidate_list:
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        # If candidate name is not in the list, put the name in the list 
        else:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 1

        # Loop through each candidate in vote summary and get he percentage of votes each candidate won
    for key, value in candidate_votes.items():
        votes_count.append(value)
        votes = candidate_votes[candidate_name]
        percentage_voted = round((int(value)/ total_vote * 100),2)
        percentage_voted_list.append(percentage_voted)

        # Determine the winner by comparing votes count for each candidate
        if (value > winner_votes_count):
            winner_votes_count = value
            winner= key
    
    # Combine 3 lists as 1 list to print
    cleaned_output = zip(candidate_list,percentage_voted_list, votes_count)
    cleaned_output = list(cleaned_output)

    # Printing Statements
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes :  {total_vote}')
    print("-------------------------")
    for item in cleaned_output:
        print(f'{item[0]} : {item[1]}% ({item[2]})')
    print("-------------------------")
    print(f'Winner : {winner}')
    print("-------------------------")

# File Output
output_path = os.path.join("/Users/drew/HW3-python-challenge/PyPoll/Analysis/HW3PyPoll.txt")

with open(output_path,'w') as f:

    f.write("Election Results")
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write(f'Total Votes :  {total_vote}')
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    for item in cleaned_output:
        f.write(f'{item[0]} : {item[1]}% ({item[2]}) ')
    f.write("\n")
    f.write("-------------------------")
    f.write("\n") 
    f.write(f'Winner : {winner}')
    f.write("\n")
    f.write("-------------------------") 