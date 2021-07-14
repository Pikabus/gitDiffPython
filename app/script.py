import os

from difflib import Differ

from services import define_result_file_name, save_result_of_comparison


file1_path = "files/file1.txt"
file2_path = "files/file2.txt"


# Open 1st file
file1 = open(file1_path, "r").readlines()
file1_name = os.path.basename(file1_path)

# Open 2nd file
file2 = open(file2_path, "r").readlines()
file2_name = os.path.basename(file2_path)


# Compare files
result_of_comparison = list(Differ().compare(file1, file2))

# Save result of comparasion
save_result_of_comparison(file1_name, file2_name, result_of_comparison)
