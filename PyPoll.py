import csv
import os


# The data we need to retrieve

# Assign a varible to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file
    headers = next(file_reader)
    print(headers)





# 1. The total number of votes case
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each cadidate won
# 4. The total number of cotes each candidate won
# 5. The winner of the election based on popular vote