input_file = "day08/input.txt"
test_input_file = "day08/test_input.txt"


def scan_tress(mapdata: list):
    print("+++ Scanning map +++\n{}\n+++  End of Map  +++\n".format(mapdata))
    width = len(mapdata[0])
    height = len(mapdata)
    print("Grid is {}x{}".format(width, height))
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
            while index >= 0:
                up.append(int(mapdata[index][col]))

                index -= 1

            # look down and compare
            down = []
            index = row+1
            while index <= height-1:
                down.append(int(mapdata[index][col]))
                index += 1

            # look left
            left = []
            index = col - 1
            while index >= 0:
                left.append(int(mapdata[row][index]))
                index -= 1

            # look right
            right = []
            index = col + 1
            while index <= width - 1:
                right.append(int(mapdata[row][index]))
                index += 1

            col += 1
        print("{} complete".format(row+1))
        row += 1


if __name__ == "__main__":
    mapdata = open(test_input_file).read().strip().splitlines()
    scan_tress(mapdata)
