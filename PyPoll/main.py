import os
import csv
import collections
number = collections.Counter()

csvelection = os.path.join('..','Resources','election_data.csv')
with open(csvelection) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader, None)
 
 #inizialize vote
    total_votes_count = 0

    Charls_vote = 0
    Diana_vote = 0
    rymon_vote = 0

    for row in csvreader:

        total_votes_count += 1

        if row[2] == "Charles Casper Stockham":
            Charls_vote += 1
        elif row[2] == "Diana DeGette":
            Diana_vote += 1
        elif row[2] == "Raymon Anthony Doane":
            rymon_vote += 1

    Results = {"Charles Casper Stockham":Charls_vote, "Diana DeGette":Diana_vote, "Raymon Anthony Doane":rymon_vote}

#calculate percentage

    Charls_Percent = round((Charls_vote / total_votes_count) * 100, 3)
    Diana_Percent = round((Diana_vote / total_votes_count) * 100, 3)
    rymon_Percent = round((rymon_vote / total_votes_count) * 100, 3)

    Winner = max(Results, key=Results.get)

    toprint = f"""Election Results
-----------------------
Total Votes: {total_votes_count} 
-----------------------
Charles Casper Stockham: {Charls_Percent}% ({Charls_vote})
Diana DeGette: {Diana_Percent}% ({Diana_vote})
Raymon Anthony Doane: {rymon_Percent}% ({rymon_vote})

-----------------------
Winner: {Winner} 
-----------------------"""
#sending txt file to analysis folder

output_path = os.path.join("..", "analysis", "output.txt")

with open(output_path, 'w', newline='') as file:

# print to Terminal
    print(toprint)

# create txt file, print to it, and close
#file = open("PyPoll.txt", "w")
    file.write(toprint)
#file.close()

