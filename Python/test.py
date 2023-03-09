import os

# Get the list of files in the current directory
files = os.listdir("./Python")

for file in files:
    # Check if the file name starts with "data_"
    if file.startswith("data_"):
        # If it does, print the file name
        print(type(file))
