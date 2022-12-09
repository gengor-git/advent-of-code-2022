
def move_through_grid(move_set: list, knot_count=2) -> int:
    rope = [(0, 0) for _ in range(knot_count)]
    trail = {(0, 0)}

    _moves_mapping = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }

    def _move_by_cords(coords: tuple, move: str) -> tuple:
        return tuple(map(lambda i, j: i + j, coords, _moves_mapping[move]))
        
    def _distance(me: tuple, other: tuple) -> tuple:
        return other[0]-me[0], other[1]-me[1]


    for move, steps in move_set:
        while steps > 0:
            print("\n\nMovement {} by {}".format(move, steps))
            print("Knot Count: {}\n".format(knot_count))
            rope[0] = _move_by_cords(rope[0], move)
            for index in range(1, knot_count):
                print("\nIndex {} : previous {} ... this one {}".format(index, rope[index], rope[index-1]))
                dx, dy = _distance(rope[index], rope[index-1])
                print("Distance: {:2d} {:2d}".format(dx, dy))

                if abs(dx) == 2 or abs(dy) == 2:
                    if dx == 0 or dy == 0:
                        print("» Standard Move {:2d} {:2d}".format(dx, dy))
                        rope[index] = _move_by_cords(rope[index], move)
                    elif dx == 1:
                        print("» Move right in addition {:2d} {:2d}".format(dx, dy))
                        rope[index] = _move_by_cords(rope[index], move)
                        rope[index] = _move_by_cords(rope[index], "R")
                    elif dx == -1:
                        print("» Move left in addition {:2d} {:2d}".format(dx, dy))
                        rope[index] = _move_by_cords(rope[index], move)
                        rope[index] = _move_by_cords(rope[index], "L")
                    elif dy == 1:
                        print("» Move down in addition {:2d} {:2d}".format(dx, dy))
                        rope[index] = _move_by_cords(rope[index], move)
                        rope[index] = _move_by_cords(rope[index], "D")
                    elif dy == -1:
                        print("» Move up in addition {:2d} {:2d}".format(dx, dy))
                        rope[index] = _move_by_cords(rope[index], move)
                        rope[index] = _move_by_cords(rope[index], "U")
                    else:
                        print("ERROR")
                        print(rope)
                else:
                    print("» No move needed for x:{} y:{}".format(dx, dy))

                print("»» New coords x:{} y:{}".format(rope[index][0], rope[index][1]))

            # we make a copy of the tupble
            trail.add(rope[-1]+tuple())

            steps -= 1
    # print("Trail: {}".format(trail))
    print(rope)
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
    # print("»»» TEST Results part 1: {} «««".format(move_through_grid(move_set, knot_count=10)))

    # move_set = load_data(input_file)
    # print("Raw move set list: {}".format(data_raw))
    # print("Adv move set list: {}".format(move_set))
    # print("»»» Results part 1: {} «««".format(move_through_grid(move_set)))

    # print("Raw move set list: {}".format(data_raw))
    # print("Adv move set list: {}".format(move_set))
    print("»»» Results part 2: {} «««".format(move_through_grid(move_set, knot_count=2)))
