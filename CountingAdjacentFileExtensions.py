import os

# Find the current route
current_route = os.getcwd()
print("your current route: ", current_route)
# List of files and folders in the current route
file_list = os.listdir(current_route)
print("list of adjacent file: ", file_list)
file_count_dict = {}
for file in file_list:
    # Find the path of the files
    file_path = os.path.join(current_route, file)
# Check that the file is  and   extension '.' has it
    if os.path.isfile(file_path) and '.' in file:
        extension = file.split('.')[-1]
        if extension in file_count_dict:
            file_count_dict[extension] += 1
        else:
            file_count_dict[extension] = 1
print("the number of files with extensions: ")
for extension, count in file_count_dict.items():
    print(extension + ':' + str(count))
