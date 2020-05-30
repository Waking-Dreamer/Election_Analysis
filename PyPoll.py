#Add deoendencies
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initalize variable and set to 0
total_votes = 0

#Create candidate list
candidate_options = []

#Create candidate directionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage= 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Skip header row?
    headers = next(file_reader)

    # print each row in csv file
    for row in file_reader:
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidates...
        if candidate_name not in candidate_options:
        
            #Add it to the list of candidates
            candidate_options.append(candidate_name)      

            #Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        #increase candidate vote count by 1
        candidate_votes[candidate_name] += 1

    #determine the % of votes for each cand by looping through counts
    #iterate through the candidate list
    for candidate in candidate_votes:
            
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate]

        #calculate the % of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")


        #Determine winning vote count and candidate
        #Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #if true, set winnning_count = to votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            #Set the winning_cadidate equal to the candidate's name

            winning_candidate = candidate

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote