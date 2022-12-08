input_file = "day08/input.txt"
test_input_file = "day08/test_input.txt"


def scan_tress(mapdata: list) -> tuple:
    print("+++ Scanning map +++\n{}\n+++  End of Map  +++\n".format(mapdata))
    width = len(mapdata[0])
    height = len(mapdata)
    print("Grid is {}x{}".format(width, height))
    visible_trees = 2*width + 2*(height-2)
    tree_views = []
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
            up_view = 0
            index = row-1
            is_visible = False
            while index >= 0:
                up.append(int(mapdata[index][col]))
                index -= 1

            if max(up) < this_tree:
                print("({} / {}) is visible from top.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            for tree in up:
                if tree < this_tree:
                    up_view += 1
                elif tree >= this_tree:
                    up_view += 1
                    break

            # look down and compare
            down = []
            down_view = 0
            index = row+1
            while index <= height-1:
                down.append(int(mapdata[index][col]))
                index += 1

            if not is_visible and max(down) < this_tree:
                print("({} / {}) is visible from bottom.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            for tree in down:
                if tree < this_tree:
                    down_view += 1
                elif tree >= this_tree:
                    down_view += 1
                    break

            # look left
            left = []
            left_view = 0
            index = col - 1
            while index >= 0:
                left.append(int(mapdata[row][index]))
                index -= 1

            if not is_visible and max(left) < this_tree:
                print("({} / {}) is visible from left.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            for tree in left:
                if tree < this_tree:
                    left_view += 1
                elif tree >= this_tree:
                    left_view += 1
                    break

            # look right
            right = []
            right_view = 0
            index = col + 1
            while index <= width - 1:
                right.append(int(mapdata[row][index]))
                index += 1

            if not is_visible and max(right) < this_tree:
                print("({} / {}) is visible from right.".format(col+1, row+1))
                is_visible = True
                visible_trees += 1

            for tree in right:
                if tree < this_tree:
                    right_view += 1
                elif tree >= this_tree:
                    right_view += 1
                    break

            tree_views.append(up_view * down_view * right_view * left_view)

            col += 1
        print("{} complete".format(row+1))
        row += 1
    return (visible_trees, tree_views)


if __name__ == "__main__":
    mapdata = open(input_file).read().strip().splitlines()
    print("Part 1: {}".format(scan_tress(mapdata)[0]))
    print("Part 2: {}".format(max(scan_tress(mapdata)[1])))
