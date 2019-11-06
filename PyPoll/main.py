# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import needed libraries
import os
import csv

# set path for import and exported files
file_to_import = os.path.join("election_data.csv")
output_file = os.path.join("poll_analysis.txt")

# define variables
total_votes = 0
candidates = []
candidate_votes = {}
votes_percentage = {}
winner = ""
max_votes = 0

with open(file_to_import) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)
    #print(header)

    #remove header from the analysis

    for row in reader:
        #increment votes
        total_votes = total_votes + 1

        candidate_name = row[2]
        #add candidate to list of candidates if they aren't there
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # increment vote for the candidate
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
    output_info = (
    f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f""
)
    # calculate percentages
    for candidate in candidate_votes:
        # collect votes as percentages
        votes = candidate_votes.get(candidate)
        votes_percentage[candidate] = round(votes/total_votes*100,2)

        # append data to output file
        output_info = output_info + f"{candidate}: {votes}, {votes_percentage[candidate]}%\n"
        #check to see if candidate has largest amount of votes
        if votes > max_votes:
            max_votes = votes
            winner = candidate


    #add winner to the output report
    output_info = output_info + ("-------------------------\n"
                                f"Winner: {winner}")

print(output_info)
with open(output_file, "w") as txt_file:
    txt_file.write(output_info)
