import re

input_file = "./day07/input.txt"
test_input_file = "./day07/test_input.txt"


class FileNode:
    def __init__(self, name, parent="None", size=0, is_dir=False) -> None:
        self.name = name
        self.parent = parent
        self.files = []
        self.directories = []
        self.size = size
        self.is_dir = is_dir
        self.part1 = 0

    def add_child(self, child):
        if child.is_dir:
            self.directories.append(child)
        else:
            self.files.append(child)
        self.size += child.size
        print("Increase size by '{}' to '{}' for '{}' with child '{}'".format(
            child.size, self.size, self.name, child.name))


def read_drive(data: list) -> FileNode:
    root = None
    current_dir = None
    current_parent = None
    for line in data:
        if line == "$ cd /":
            print("We are at root.")
            root = FileNode("/", None, 0, True)
            current_dir = root
        elif line == "$ ls":
            pass
        elif line.startswith("$ cd"):
            if line.endswith(".."):
                print("Move UP from {} to {}.".format(
                    current_dir.name, current_parent.name))
                if current_dir.size <= 100000:
                    root.part1 += current_dir.size
                current_parent.add_child(current_dir)
                current_dir = current_parent
                if current_parent == root:
                    current_parent = None
                else:
                    current_parent = current_parent.parent
                # print("DEBUG {}".format(line))
                # print("Moving up to {}".format(current_dir.name))
            else:
                # new dir
                _, _, name = line.split()
                go_to_dir = FileNode(name, parent=current_dir, is_dir=True)
                print("Move DOWN from '{}' into '{}'".format(
                    current_dir.name, go_to_dir.name))
                current_parent = current_dir
                current_dir = go_to_dir
        elif re.findall(r"^([0-9]*) ([a-z.]*)$", line):
            # print(line)
            size, name = line.split()
            this_file = FileNode(name, parent=current_dir,
                                 size=int(size), is_dir=False)
            current_dir.add_child(this_file)
        elif re.findall(r"dir [\w]*", line):
            print("'{}' is just a dir.".format(line))

    print("Finishing up.")
    current_parent.add_child(current_dir)
    if current_dir.size <= 100000:
        root.part1 += current_dir.size
    if current_parent != root:
        root.add_child(current_parent)
        if current_parent.size <= 100000:
            root.part1 += current_parent.size

    return root


if __name__ == "__main__":
    data = open(input_file).read().strip().splitlines()
    resultPart1 = read_drive(data).part1
    print("Result part 1: {}".format(resultPart1))
