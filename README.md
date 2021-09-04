# **Election Analysis**

## **_Overview of the Audit_**

We were brought on by Seth and Tom to create a Python code that would automatically parse through the election results by county and candidate. Ultimately, the purpose of the code is to output the election results onto a text file. The desired metrics to be outputted were as follows: *Total Number of Votes Cast, Votes Cast by County, Percentage of Votes Cast by County, The Largest Turnout Within the Election, The Number of Votes Received by Each Candidate, The Percentage of Total Votes Received By Each Candidate, The Winner of the Election, The Number of Votes Received by the Winner, and the Percentage of Votes Received by the Winner.* 

Given the laborious nature of tabulating votes by hand, our code will be utilized in this and all future elections to assist the State in calculating vote totals and outcomes. 

### **_Election Outcomes_**

Using our code, we noted the following:

- *How many votes were cast in this congressional election?*

    In order to calculate this total, we first had to intialize the total votes variable at zero:
    
    ```
    # 1. The total number of votes cast
    total_votes = 0
    ```
    Thereafter, we had are code parse through each row of the election outcomes file (ensuring that it skips the header row) and count each instance of a vote cast by increasing the aforementioned total votes variable by 1 every time a row was noted:

    ```
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
    ```
    
    This ultimately yielded the total number of votes cast: **369,711**


- *Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.*

    In order to perform this function, we had to do a few things. First, we created an empty list to ultimately contain the names of each county within the election, as well as an empty dictionary to hold the county names as keys and the number of votes cast within each county as corresponding values:

    ```
    # 1: Create a county list and county votes dictionary.
    county_list = []
    county_votes = {}
    ```

    Thereafter, using the For loop referenced above, we had the code parse through all rows of the election file. Given that each row is effectively a list, with the columns representing the Ballot ID (0), the County (1), and the Candidate (2), we referenced the index value for the County (1) to extract the county name from each vote:

    ```
    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
    ```

    In order to ensure that the same county is not listed multiple times over, we created a new conditional statement to determine whether (as the code is going through each row) the county has already been added to the list (and if it has not, to add it). Within this loop, we also had the code access the county_votes dictionary that was previously created, defined the values as the county names for this dictionary, and initialized the values (which correspond to the votes) at zero. We then exited the conditional statement and, while under the loop going through the rows of the spreadsheet, increased the vote total for each county by 1 whenever that county was refenced in a row:

    ```
    if county_name not in county_list:


            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
    ```
    
    This effectively tabulated the total votes received from each county. To calculate the percentage, we initialized a new loop (this time, looping through the values of the county votes dictionary), we created a new variable to access the county_votes dictionary and store its values (votes), and while looping through of the three counties, had our code divide the votes from each county by the total number of votes (see above):

    ```
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percent = float(county_vote_count) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_vote_percent:.1f}% ({county_vote_count:,})\n")

        # 6d: Print the county results to the terminal.
        print(county_results)
    ```

    The above code yielded the following results:

    (a) **Jefferson: 10.5% (38,855)**

    (b) **Denver: 82.8% (306,055)**

    (c) **Arapahoe: 6.7% (24,801)**


 
- *Which county had the largest number of votes?*

    In order to determine this, we first had to create an empty string variable to contain the largest county, and set a variable to initialize the largest county turnout to zero:

    ```
    # 2: Track the largest county and county voter turnout.
    largest_county = ""
    largest_turnout = 0
    ```

    Once this was done, we added a new conditional statement under the above-referenced loop (the one looping through the dictionary values). The purpose of this conditional was to increase the largest_turnout variable for each county to each county's total number of votes, and then have the conditional statement locate the county with the greatest overall turnout:

    ```
     # 6f: Write an if statement to determine the winning county and get its vote count.
        if county_vote_count > largest_turnout:
            largest_turnout = county_vote_count
            largest_county = county_name

        largest_county_results = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n")
    ```

    The output yielded that **Denver** county had the largest turnout. 

- *Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.*

    The process to calculate and output candidate information is effectively analagous to the process for calculating the county metrics that was discussed above. As such, please refer to the **APPENDIX** on the bottom of this analysis for a complete breakdown of the code. 

    Our code yielded the following output:

    (a) **Charles Casper Stockham: 23.0% (85,213)**

    (b) **Diana DeGette: 73.8% (272,892)**

    (c) **Raymon Anthony Doane: 3.1% (11,606)**


- *Which candidate won the election, what was their vote count, and what was their percentage of the total votes?*

    As noted above, please refer to the **APPENDIX** for the complete breakdown of the code.

    Our code yielded the following output:

    (a) Winner: Diana DeGette

    (b) Winning Vote Count: 272,892

    (c) Winning Percentage: 73.8%

## **_Election Audit Summary_**

We hope that the Election Committee is satisfied with out script and its output. It is our hope that this script may be utilized for future statewide elections. As the script has been written to loop through all of the rows of the election file, it should be easily scalable and can be used to tabulate any election result (so long as the CSV election file that the script is parsing through is organized in the same structure as the original file that was utilized). 

There are some important things to be aware of (specifically, how the script can be modified to be used for future elections):

- The following code was utilized the define the path of the input file (the CSV election file), as well as the ultimate outpute file. In order to be used for future elections, it is crucial that the path be updated in order to access the correct readable file:

    ```
    # Add a variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
    # Add a variable to save the file to a path.
    file_to_save = os.path.join("analysis", "election_analysis.txt")
    ```

- Additionally, depending on the type of election that the script is being utilized for, it is also important to ensure that all of the variable names and output/print instructions remain consistent. For example, if the "County" is no longer being tracked and some other metric is being utilized, then the variable names should be updated to reflect this. Also, if the columns are not in the same order (say, county and cadidate name are reserved), it's also important to ensure that the index values used to access this information within the code are updated to match the correct position of the information within the file. 

- Lastly, as a future idea, columns may be added to denote the method of the casted vote (i.e. mail in ballot, electronic, etc.). That way, the same code format may be utilized, but variables, lists and dictionaries may be added to calculate totals and percentages by type of vote (in case those statistics are required). 

# **APPENDIX**

## **_Complete Extract of Script_**

```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}



# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_turnout = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.

        if county_name not in county_list:


            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percent = float(county_vote_count) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county_vote_percent:.1f}% ({county_vote_count:,})\n")

        # 6d: Print the county results to the terminal.
        print(county_results)

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if county_vote_count > largest_turnout:
            largest_turnout = county_vote_count
            largest_county = county_name

        largest_county_results = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"-------------------------\n")


    # 7: Print the county with the largest turnout to the terminal.
    print(largest_county_results)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_results)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```







