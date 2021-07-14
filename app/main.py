import os
import sys
import mimetypes

from difflib import Differ

from services import define_result_file_name, save_result_of_comparison, check_is_file_text


# Open 1st file
while True:
    file1_path = input("Input the path of the first file: ")
    file1_path = check_is_file_text(file1_path)
    try:
        file1 = open(file1_path, "r").readlines()
        break
    except FileNotFoundError:
        print(f"Error! File {file1_path} doesn't exists!")
file1_name = os.path.basename(file1_path)

# Open 2nd file
while True:
    file2_path = input("Input the path of the second file: ")
    file2_path = check_is_file_text(file2_path)
    try:
        file2 = open(file2_path, "r").readlines()
        break
    except FileNotFoundError:
        print(f"Error! File {file2_path} doesn't exists!")
file2_name = os.path.basename(file2_path)

# Compare files
result_of_comparison = list(Differ().compare(file1, file2))

# Save result of comparasion
save_result_of_comparison(file1_name, file2_name, result_of_comparison)