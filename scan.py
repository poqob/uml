# Import the required modules
import os
import sys
import subprocess

# Check if the folder is given as a parameter
if len(sys.argv) < 2:
    print("Usage: python script.py folder")
    exit()

# Get the folder path
folder = sys.argv[1]

# Check if the folder exists
if not os.path.isdir(folder):
    print("Invalid folder")
    exit()

# Create a list to store the plantuml files
plantuml_files = []

# Walk through the folder and find the plantuml files
for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".plantuml"):
            # Get the full path of the file
            file_path = os.path.join(root, file)
            # Append the file to the list
            plantuml_files.append(file_path)

# Check if any plantuml file is found
if not plantuml_files:
    print("No plantuml file found in the folder")
    exit()

# Create a list to store the png files
png_files = []

# Loop through the plantuml files and generate the png files
for plantuml_file in plantuml_files:
    # Get the file name without extension
    file_name = os.path.splitext(os.path.basename(plantuml_file))[0]
    # Create the png file name
    png_file = file_name + ".png"
    # Run the plantuml command to generate the png file from the plantuml file¹[1]
    subprocess.run(["plantuml", "-o", png_file, plantuml_file])
    # Append the png file to the list
    png_files.append(png_file)

# Print the png files
print("The following png files are generated:")
for png_file in png_files:
    print(png_file)
