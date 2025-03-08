import os
import re

# Script that renames files in the current directory, and subdirectories, to the format YYYY-MM-DD


# Example filename: "25-12-2023, vacation_photo.jpg"
# Regex pattern to match filenames with a date format "DD-MM-YYYY,"
pattern = re.compile(r'^(\d{2})-(\d{2})-(\d{4}),\s(.*)$')

def rename_files():
    # Supported file extensions
    valid_extensions = {"png", "gif", "jpg", "jpeg"}
    
    directory = os.getcwd()
    
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            
            # Ensure it's a file and has a valid image extension
            if filename.lower().split(".")[-1] in valid_extensions:
                match = pattern.match(filename)
                
                if match:
                    day, month, year, rest_of_name = match.groups()
                    
                    # Convert date to YYYY-MM-DD format
                    new_date = f"{year}-{month}-{day}"
                    
                    # Construct new filename
                    new_filename = f"{new_date}, {rest_of_name}"
                    new_filepath = os.path.join(root, new_filename)
                    
                    # Rename file
                    os.rename(filepath, new_filepath)
                    print(f"Renamed: {filepath} -> {new_filepath}")

if __name__ == "__main__":
    rename_files()
