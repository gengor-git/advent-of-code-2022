
def move_through_grid(move_set: list) -> int:
    loc_head, loc_tail = (0, 0), (0, 0)
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
        # print("Moving [ {} ] by [ {:2d} ] steps ...".format(move, steps))
        while steps > 0:
            loc_head = _move_by_cords(loc_head, move)
            # print("                   ├[ {} ]-({:4d}/{:4d})".format(move,
            #   position_h[0], position_h[1]))

            dx, dy = _distance(loc_tail, loc_head)
            print("\nDistance: {:2d} {:2d}".format(dx, dy))

            if abs(dx) == 2 or abs(dy) == 2:
                if dx == 0 or dy == 0:
                    print("» Standard Movelv{:2d} {:2d}".format(dx, dy))
                    loc_tail = _move_by_cords(loc_tail, move)
                elif dx == 1:
                    print("» Move right in addition {:2d} {:2d}".format(dx, dy))
                    loc_tail = _move_by_cords(loc_tail, move)
                    loc_tail = _move_by_cords(loc_tail, "R")
                elif dx == -1:
                    print("» Move left in addition {:2d} {:2d}".format(dx, dy))
                    loc_tail = _move_by_cords(loc_tail, move)
                    loc_tail = _move_by_cords(loc_tail, "L")
                elif dy == 1:
                    print("» Move down in addition {:2d} {:2d}".format(dx, dy))
                    loc_tail = _move_by_cords(loc_tail, move)
                    loc_tail = _move_by_cords(loc_tail, "D")
                elif dy == -1:
                    print("» Move up in addition {:2d} {:2d}".format(dx, dy))
                    loc_tail = _move_by_cords(loc_tail, move)
                    loc_tail = _move_by_cords(loc_tail, "U")
                else:
                    print("ERROR")
            else:
                print("» No move needed for x:{} y:{}".format(dx, dy))

            print("»» New coords x:{} y:{}".format(loc_tail[0], loc_tail[1]))

            # we make a copy of the tupble
            trail.add(loc_tail+tuple())

            steps -= 1
    # print("Trail: {}".format(trail))
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
    print("»»» TEST Results part 1: {} «««".format(move_through_grid(move_set)))

    move_set = load_data(input_file)
    # print("Raw move set list: {}".format(data_raw))
    # print("Adv move set list: {}".format(move_set))
    print("»»» Results part 1: {} «««".format(move_through_grid(move_set)))
