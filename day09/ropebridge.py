
def move_through_grid(move_set: list, knot_count=2) -> int:
    ropes = [(0, 0) for _ in range(knot_count)]
    trail = {(0, 0)}

    _moves_mapping = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }

    def _move_by_direction(coords: tuple, move: str) -> tuple:
        return tuple(map(lambda i, j: i + j, coords, _moves_mapping[move]))

    def _move_by_pre(my_location: tuple, predecessor: tuple) -> tuple:
        x, y = my_location
        a, b = predecessor
        dx, dy = _distance(my_location, predecessor)
        j, k = 0, 0
        # print("Move by predecessor x:{} y:{} ... a:{} b:{}".format(x, y, a, b))
        # print("Distance: {:2d} {:2d}".format(dx, dy))
        
        if abs(dx) == 2 and abs(dy) == 2:
            print("A", end="...")
            j = x + 1 if dx > 0 else x - 1
            k = y + 1 if dy > 0 else y - 1
        elif abs(dx) == 2 and abs(dy) == 1:
            print("B", end="...")
            j = x + 1 if dx > 0 else x - 1
            k = y + 1 if dy > 0 else y - 1
        elif abs(dx) == 1 and abs(dy) == 2:
            print("C", end="...")
            j = x + 1 if dx > 0 else x - 1
            k = y + 1 if dy > 0 else y - 1
        elif abs(dx) == 2 and abs(dy) == 0:
            print("D", end="...")
            j = x + 1 if dx > 0 else x - 1
            k = y
        elif abs(dx) == 0 and abs(dy) == 2:
            print("E", end="...")
            j = x
            k = y + 1 if dy > 0 else y - 1
        elif dx == 0 and dy == 0 or abs(dx) == 1 and abs(dy) == 1:
            j = x
            k = y
        else:
            print("ERROR??", end="...")
            j = x
            k = y
        
        print("Old [{}] [{}] . Pre [{}][{}] . New [{}] [{}]".format(x, y, a, b, j, k))

        return j, k
        
    def _distance(me: tuple, other: tuple) -> tuple:
        return other[0]-me[0], other[1]-me[1]


    for move, steps in move_set:
        print("\n\nMovement {} by {}".format(move, steps))
        while steps > 0:
            ropes[0] = _move_by_direction(ropes[0], move)
            for index in range(1, knot_count):
                ert = _move_by_pre(ropes[index], ropes[index-1])
                ropes[index] = ert

            # we make a copy of the tupble
            trail.add(ropes[-1])

            steps -= 1
    # print("Trail: {}".format(trail))
    print(ropes)
    return len(trail)


def load_data(textfile) -> list:
    data_raw = [list(line.split()) for line in open(
        textfile).read().strip().splitlines()]
    move_set = []
    for direction, steps in data_raw:
        # print("Direction: {}, Steps: {}".format(direction, steps))
        move_set.append((direction, int(steps)))
    print(len(move_set))
    return move_set


if __name__ == "__main__":
    input_file = "day09/input.txt"
    test_input_file = "day09/test_input.txt"

    move_set = load_data(test_input_file)
    # print("Raw move set list: {}".format(data_raw))
    # print("Adv move set list: {}".format(move_set))
    print("»»» TEST Results part 1: {} «««".format(move_through_grid(move_set, knot_count=10)))

    move_set = load_data(input_file)
    # print("Raw move set list: {}".format(data_raw))
    # print("Adv move set list: {}".format(move_set))
    print("»»» Results part 1: {} «««".format(move_through_grid(move_set)))

    # print("Raw move set list: {}".format(data_raw))
    # print("Adv move set list: {}".format(move_set))
    print("»»» Results part 2: {} «««".format(move_through_grid(move_set, knot_count=10)))
