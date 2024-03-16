import os
import csv

# Get the current directory
current_directory = os.getcwd()

# Define the folder name containing the CSV files
folder_name = 'csv'

# Construct the full path to the CSV folder
folder_path = os.path.join(current_directory, folder_name)

# Normalize the path
folder_path = os.path.normpath(folder_path)

# List all files in the folder
file_names = os.listdir(folder_path)

# Iterate over each file in the folder
for file_name in file_names:
    # Check if the file is a CSV file
    if file_name.endswith('.csv'):
        # Construct the full path to the CSV file
        file_path = os.path.join(folder_path, file_name)

        # Open the CSV file and read its contents
        with open(file_path, 'r', newline='') as file:
            # Create a CSV reader object
            reader = csv.reader(file)

            # Read and process each row in the CSV file
            for row in reader:
                # Do something with each row, for example, print it
                print(row)
input("Press to continue")