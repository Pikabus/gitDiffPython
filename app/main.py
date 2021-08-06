import os

from difflib import Differ

from config import PATH_OF_RESULTS_FOLDER


def check_file_exists(file_number: str) -> str:
    while True:
        file_path = input(f"Input the path of the {file_number} file: ")
        try:
            open(file_path, "r").readlines()
            break
        except UnicodeDecodeError:
            file_name = os.path.basename(file_path)
            print(f"{file_name} is not a text file!")
            os.sys.exit()
        except FileNotFoundError:
            print(f"Error! File {file_path} doesn't exists!")
    return file_path


def get_file_name(file_full_name: str) -> str:
    file_full_name = file_full_name[::-1]
    file_name = file_full_name[file_full_name.find(".")+1:]
    file_name = file_name[::-1]
    return file_name


def get_file_extension(file_full_name: str) -> str:
    file_full_name = file_full_name[::-1]
    if file_full_name.find(".") != -1:
        file_extension = file_full_name[:file_full_name.find(".")]
        file_extension = file_extension[::-1]
    else:
        file_extension = ""
    return file_extension


def define_result_file_name(file_full_name: str) -> str:
    file_name = get_file_name(file_full_name)
    file_extension = get_file_extension(file_full_name)
    result_file_name = file_name + "." + file_extension

    # Defining the file name in results folder by setting (копия X) if it exists
    copy_number_counter = 0
    while True:
        if result_file_name in os.listdir(f"{PATH_OF_RESULTS_FOLDER}"):
            file_name = file_name.replace(
                f"_(копия {copy_number_counter})", "")
            copy_number_counter += 1
            file_name += f"_(копия {copy_number_counter})"
            result_file_name = file_name + "." + file_extension
        else:
            break
    return result_file_name


def save_result_of_comparison(first_file_path: str, second_file_path: str, result_of_comparison: list) -> None:
    first_file_name = os.path.basename(first_file_path)
    second_file_name = os.path.basename(second_file_path)
    result_file_name = f"Comparison_result_{first_file_name}_and_{second_file_name}.diff"
    result_file_name = define_result_file_name(result_file_name)

    result_relative_path = f"{PATH_OF_RESULTS_FOLDER}{result_file_name}"

    with open(result_relative_path, "w") as result_file:
        comparison_result_str = ''.join(str(elem)
                                        for elem in result_of_comparison)
        result_file.write(comparison_result_str)
        print(f"Result of the comparison files in {result_relative_path}")


def compare_files(first_file_path: str, second_file_path: str) -> str:
    # Compare files and save result
    first_file_content = open(first_file_path, "r").readlines()
    second_file_content = open(second_file_path, "r").readlines()
    result_of_comparison = list(Differ().compare(first_file_content,
                                                 second_file_content))
    return result_of_comparison


if __name__ == "__main__":
    file_number = "first"
    first_file_path = check_file_exists(file_number)
    file_number = "second"
    second_file_path = check_file_exists(file_number)

    result_of_comparison = compare_files(first_file_path, second_file_path)
    save_result_of_comparison(first_file_path,
                              second_file_path, result_of_comparison)
