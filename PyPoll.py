# Retrieve Data
import csv
import os

# Assign a variable to upload the file from the path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# Assign a variable to save the file to the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: Read and Analyze data.
    file_reader = csv.reader(election_data)

# Print each row in the CSV file.
  #  for row in file_reader:
    headers = next(file_reader)
    print(headers)

#Use the with statement to open/and close the file as a text file.
#with open(file_to_save, 'w') as txt_file:

# Write three counties to the file.
 #   txt_file.write('Counties in the Election\n\n')
 #   txt_file.write('Arapahoe\nDenver\nJefferson')

#Open the file with the open() function 'w' as the mode: to write data to the file

# 1. The total # of votes cast

# 2. A complete list of candidates who recieved votes

# 3. Total # of votes ezch candidate received

# 4. % of votes each candidate won

# 5. The winner of the election based on popular vote

