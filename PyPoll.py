import csv
import os


# The data we need to retrieve

# Assign a varible to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")


# 1. The total number of votes cast
total_votes = 0

# Create the candidate_options list so that we can later store values into it
candidate_options = []

 # Create a dictionary where the key is candidate name and value is total votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    headers = next(file_reader)
    
    for row in file_reader:
        # For each row in the file not including the header (representing one vote), add to "0" until all rows are spent.
        # This is the total number of votes
        total_votes += 1
        
        # Define the index where candidate names are located within the read file
        candidate_name = row[2]

        
        # Conditional statig that as the function loops through the rows, if it finds a name that hasn't already been added
        # to candidate_options list, it will add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Begin tracking candidate votes. This belongs here because we are initializing candidate votes at 0
            # once the candidate is added to candidate options (which has a unique value). Otherwise, if this went
            # outside of the if function, then the candidate votes would be reset to zero after each row, and now
            # after each candidate name:
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"---------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        votes_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)
        

        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = candidate_name
            
    winning_candidate_summary = (
        f"---------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------------------\n"
    )

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)








