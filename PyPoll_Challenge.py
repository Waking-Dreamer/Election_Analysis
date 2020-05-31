#Add dependencies
import csv
import os

#assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initalize variable and set to 0
total_votes = 0

#Create candidate list, and candidate dictionary
candidate_options = []
candidate_votes = {}

#create county list and couty_votes dict
counties = []
county_votes = {}

#Winning Candidate, Winning Count, winning % Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Empty string to hold county with largest turnout
largest_turnout = ""
largest_turnout_count = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # read the header row
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

        #Print county from each row
        county_name = row[1]

        #If county does not match existing county in list
        if county_name not in counties:

            # Add county to list of counties
            counties.append(county_name)

            #Begin tracking county votes
            county_votes[county_name] = 0

        #increase county vote count by 1
        county_votes[county_name] += 1

#Save results to text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results)
        
    # Save the final vote count to the text file.
    txt_file.write(election_results)

#print county votes title
    print(f"County Votes:\n", end="")
    
    #Determine the % of votes for each county by looping through counts
    #iterate through the county list
    for county in county_votes:

        #retrieve county vote count and %
        votes_per_c = county_votes[county]
        c_vote_percentage = float(votes_per_c) / float(total_votes) * 100
        county_results = (f"{county}: {c_vote_percentage:.1f}% ({votes_per_c:,})\n")

        #print each county, their vote count, and % of votes in terminal
        print(county_results, end="")

        # Save the county results to our text file.
        txt_file.write(county_results)

        #Determine county with highest turnout of voters
        if (votes_per_c > largest_turnout_count):
            largest_turnout_count = votes_per_c
            largest_turnout = county

        # Print the county with the highest turnout in terminal
        largest_county_turnout = (
            f"-------------------------\n"
            f"Largest County Turnout: {largest_turnout}\n"
            f"-------------------------\n")

    # Print blank line and county with highest turnout
    print()
    print(largest_county_turnout, end="")

    #Save the county with highest turnout to text file
    txt_file.write(largest_county_turnout)

    # determine the % of votes for each cand by looping through counts
    # iterate through the candidate list
    for candidate in candidate_votes:
                
        #retrieve vote count and %
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results, end="")
            
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    #Print the winning candidate's results in terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)