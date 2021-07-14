import os


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
        if result_file_name in os.listdir("results/"):
            file_name = file_name.replace(f" (копия {name_counter})", "")
            name_counter += 1
            file_name += f" (копия {name_counter})"
            result_file_name = file_name + "." + file_extension
        else:
            break

    return result_file_name


def save_result_of_comparison(file1_name, file2_name, result_of_comparison):
    # Saved the result of the comparison files in file named result_file_name
    result_file_name = f"Comparison_result_{file1_name}_and_{file2_name}.txt"
    result_file_name = define_result_file_name(result_file_name[::-1])

    comparison_result = ''.join(str(elem) for elem in result_of_comparison)

    with open(f"results/{result_file_name}", "w") as result_file:
        result_file.write(comparison_result)
