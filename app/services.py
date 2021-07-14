import os
import sys
import mimetypes

from config import RESULTS_FOLDER_PATH


def define_result_file_name(result_file_name: str) -> str:

    file_name = result_file_name[result_file_name.find(".")+1:]
    file_name = file_name[::-1]

    if result_file_name.find(".") != -1:
        file_extension = result_file_name[:result_file_name.find(".")]
        file_extension = file_extension[::-1]
    else:
        file_extension = ""

    result_file_name = file_name + "." + file_extension

    # Define file name. If this file name exists: file name += "file_name (копия name_counter).file_extension"
    name_counter = 0
    while True:
        if result_file_name in os.listdir(f"{RESULTS_FOLDER_PATH}"):
            file_name = file_name.replace(f" (копия {name_counter})", "")
            name_counter += 1
            file_name += f" (копия {name_counter})"
            result_file_name = file_name + "." + file_extension
        else:
            break

    return result_file_name


def save_result_of_comparison(file1_name: str, file2_name: str, result_of_comparison: list):
    # Saved the result of the comparison files in file named result_file_name
    result_file_name = f"Comparison_result_{file1_name}_and_{file2_name}.txt"
    result_file_name = define_result_file_name(result_file_name[::-1])

    comparison_result = ''.join(str(elem) for elem in result_of_comparison)
    result_relative_path = f"{RESULTS_FOLDER_PATH}{result_file_name}"

    with open(result_relative_path, "w") as result_file:
        result_file.write(comparison_result)
        result_file_abs_path = os.path.abspath(result_relative_path)
        print(f"Result of the comparison files in {result_file_abs_path}")
