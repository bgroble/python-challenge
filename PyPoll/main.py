import os
import csv

# budget_csv = os.path.join('Resources', 'budget_data.csv')
election_data = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
# print("election_data.csv resource path is:    ",election_data)

#open and read csv
with open(election_data) as csvfile:
    csv_read = csv.reader(csvfile, delimiter=',')

# read the header row first
    csv_head = next(csv_read)
    # print(f"Header: {csv_head}")
          
# read each row of data after the header
    # for row in csv_read:
    #     print(row)

# make a csvlist
    election_list = list(csv_read)
    # print(election_list[0:5])

# list of votes
votes_list = [row[2] for row in election_list]
# print(votes_list[:5])

# total number of votes cast
total_votes = len(votes_list)
print(total_votes)

# complete list of candidates who received votes
row_count = len(election_list)
candidates = list()
count = list()
for i in range(0, row_count):
    candidate_names = election_list[i][2]
    count.append(candidate_names)
    if candidate_names not in candidates:
        candidates.append(candidate_names)
print(candidates)

# count number of candidates
complete_candidates = len(candidates)
print(complete_candidates)

# total number of votes each candidate won
candi_votes = list()
percentage = list()
for j in range(0,complete_candidates):
    name = candidates[j]
    candi_votes.append(count.count(name))
print(candi_votes)

# initialize count of all candidates
Stockham_count = DeGette_count = Doane_count = 0 

# initialize percent of all candidates
Stockham_per = DeGette_per = Doane_per = 0

# loop through the row in each data set
for row in election_list:
    if row[2] == "Charles Casper Stockham":
        Stockham_count += 1
    elif row[2] == "Diana DeGette":
        DeGette_count += 1
    elif row[2] == "Raymon Anthony Doane":
        Doane_count += 1

Results_count = {"Charles Casper Stockham":Stockham_count, "Diana DeGette":DeGette_count, "Raymon Anthony Doane":Doane_count}
print(Results_count)

# calculate percentages 
Stockham_per = round((Stockham_count/total_votes)*100, 3)
print("%s%%"%Stockham_per)
DeGette_per = round((DeGette_count/total_votes)*100, 3)
print("%s%%"%DeGette_per)
Doane_per = round((Doane_count/total_votes)*100, 3)
print("%s%%"%Doane_per)

# calculate winner
winner = max(Results_count, key=Results_count.get)
# print("Winner:", winner)

# print everything nicely in terminal 
print("Election Results")
print(f"Total Votes: {total_votes}")
print(f"Charles Casper Stockham: {Stockham_per}% ({Stockham_count})")
print(f"Diana DeGette: {DeGette_per}% ({DeGette_count})")
print(f"Raymon Anthony Doane: {Doane_per}% ({Doane_count})")
print(f"Winner: {winner}")

# create output path 
output = os.path.join(os.path.dirname(__file__), "Analysis", "pypoll_text.txt")

# add to text file
with open(output, "w") as textfile:   
    textfile.write("Election Results\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Charles Casper Stockham: {Stockham_per}% ({Stockham_count})\n")
    textfile.write(f"Diana DeGette: {DeGette_per}% ({DeGette_count})\n")
    textfile.write(f"Raymon Anthony Doane: {Doane_per}% ({Doane_count})\n")
    textfile.write("-----------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-----------------------------\n")

