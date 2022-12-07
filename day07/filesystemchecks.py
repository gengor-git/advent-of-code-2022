import re

input_file = "./day07/input.txt"
test_input_file = "./day07/test_input.txt"


def create_directory_dict(data: list):
    directories, index = [{}], 0
    while index < len(data):
        command = data[index].split()
        if command[1] == "cd" and command[2] == "..":
            print("Go UP one directory")
            directories.pop()
        elif command[1] == "cd":
            target_dir = command[2]
            print("Go INTO one directory: '{}'".format(target_dir))
            if target_dir not in directories[-1]:
                directories[-1][target_dir] = {}
            # this linking is required for the pop above to work
            directories.append(directories[-1][target_dir])
        elif command[1] == "ls":
            print("Reading dir '{}'".format(data[index-1].split()[2]))
            while index + 1 < len(data) and data[index + 1][0] != "$":
                size, name = data[index + 1].split()
                print("Item: {}, {}".format(name, size))
                if size != "dir":
                    directories[-1][name] = int(size)
                else:
                    directories[-1][name] = {}
                index += 1
        else:
            print("===========> REST {}".format(command))
        index += 1
    return directories[0]


def calculate_sizes(directories):
    all_dirs = []

    def _size_per_directory(directory):
        size = 0
        for _, data in directory.items():
            if type(data) is dict:
                size += _size_per_directory(data)
            else:
                size += int(data)
        # this ensures each dir is listed separately.
        all_dirs.append(size)
        return size
    _size_per_directory(directories)
    return all_dirs


if __name__ == "__main__":
    data = open(input_file).read().strip().splitlines()
    root = create_directory_dict(data)
    sizes = sorted(calculate_sizes(root))
    part2 = 0
    storage = 70000000
    free_needed = 30000000
    current_used = sizes[-1]
    for directory in sizes:
        if storage - current_used + directory >= free_needed:
            part2 = directory
            break
    print(part2)
