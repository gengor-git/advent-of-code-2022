input_file = "day09/input.txt"
test_input_file = "day09/test_input.txt"


def move_through_grid(move_set: list) -> int:
    positions_touched = 0
    position_h, position_t = (0, 0), (0, 0)
    trail = [tuple]

    _moves_mapping = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }

    for move, steps in move_set:
        print("Moving [ {} ] by [ {:2d} ] steps ...".format(move, steps))
        while steps > 0:
            position_h = tuple(
                map(lambda i, j: i + j, position_h, _moves_mapping[move]))
            print("{}»({:3d}/{:3d})".format(move,
                  position_h[0], position_h[1]))
            steps -= 1
    return positions_touched


def load_data(inut_file) -> list:
    data_raw = [list(line.split()) for line in open(
        input_file).read().strip().splitlines()]
    move_set = []
    for direction, steps in data_raw:
        # print("Direction: {}, Steps: {}".format(direction, steps))
        move_set.append((direction, int(steps)))
    return move_set


if __name__ == "__main__":
    move_set = load_data(test_input_file)

    # print("Raw move set list: {}".format(data_raw))
    # print("Adv move set list: {}".format(move_set))
    print("»»» Results part 1: {} «««".format(move_through_grid(move_set)))
