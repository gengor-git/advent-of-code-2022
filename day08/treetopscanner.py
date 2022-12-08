input_file = "day08/input.txt"
test_input_file = "day08/test_input.txt"


def scan_tress(mapdata: list):
    print("+++ Scanning map +++\n{}\n+++  End of Map  +++\n".format(mapdata))
    width = len(mapdata[0])
    height = len(mapdata)
    print("Grid is {}x{}".format(width, height))
    visible_trees = 2*width + 2*(height-2)
    row = 1
    while row < len(mapdata)-1:
        # print("{:5d} : {}".format(row, mapdata[row]))
        col = 1
        while col < len(mapdata[row])-1:
            # print("(x:{:d} / y:{:d}) → {:s}".format(col,
            #       row, mapdata[row][col]))
            this_tree = int(mapdata[row][col])

            # look up and compare
            up = []
            index = row-1
            is_visible = False
            while index >= 0 and not is_visible:
                up.append(int(mapdata[index][col]))
                index -= 1

            if max(up) < this_tree:
                print("({} / {}) is visible from top.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            # look down and compare
            down = []
            index = row+1
            while index <= height-1 and not is_visible:
                down.append(int(mapdata[index][col]))
                index += 1

            if not is_visible and max(down) < this_tree:
                print("({} / {}) is visible from bottom.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            # look left
            left = []
            index = col - 1
            while index >= 0 and not is_visible:
                left.append(int(mapdata[row][index]))
                index -= 1

            if not is_visible and max(left) < this_tree:
                print("({} / {}) is visible from left.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            # look right
            right = []
            index = col + 1
            while index <= width - 1 and not is_visible:
                right.append(int(mapdata[row][index]))
                index += 1

            if not is_visible and max(right) < this_tree:
                print("({} / {}) is visible from right.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            col += 1
        print("{} complete".format(row+1))
        row += 1
    return visible_trees


if __name__ == "__main__":
    mapdata = open(test_input_file).read().strip().splitlines()
    print("Part 1: {}".format(scan_tress(mapdata)))
