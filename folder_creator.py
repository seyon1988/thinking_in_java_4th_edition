import os


input_file_path = './Chapters.txt'
output_directory = '.'


os.makedirs(output_directory, exist_ok=True)


with open(input_file_path, 'r') as file:
    lines = file.readlines()


for index, line in enumerate(lines, start=1):
    line = line.strip()
    folder_name = f"Chapter_{index:02}_{line}"
    output_folder_path = os.path.join(output_directory, folder_name)
    
    os.makedirs(output_folder_path, exist_ok=True)

    filename = f"{line}.txt"
    output_file_path = os.path.join(output_folder_path, filename)

    with open(output_file_path, 'w') as output_file:
        output_file.write(line)
