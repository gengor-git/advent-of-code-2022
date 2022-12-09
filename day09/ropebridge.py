
def move_through_grid(move_set: list) -> int:
    positions_touched = 0
    position_h, position_t = (0, 0), (0, 0)
    trail = {(0, 0)}

    _moves_mapping = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, -1),
        "D": (0, 1)
    }

    for move, steps in move_set:
        # print("Moving [ {} ] by [ {:2d} ] steps ...".format(move, steps))
        while steps > 0:
            position_h = tuple(
                map(lambda i, j: i + j, position_h, _moves_mapping[move]))
            # print("                   ├[ {} ]-({:4d}/{:4d})".format(move,
            #   position_h[0], position_h[1]))

            # reposition the tail now
            # xxx  (-1/-1) ( 0/-1) ( 1/-1)
            # xHx  (-1/ 0)    H    ( 1/ 0)
            # xxx  (-1/ 1) ( 0/ 1) ( 1/ 1)
            distance = ((position_h[0] - position_t[0]),
                        (position_h[1] - position_t[1]))

            need_to_move_horizontally = distance[0] < -1 or distance[0] > 1
            need_to_move_vertically = distance[1] < -1 or distance[1] > 1

            if need_to_move_vertically or need_to_move_horizontally:
                if position_h[0] == position_t[0]:
                    # same column / x : just make the same move
                    position_t = tuple(
                        map(lambda i, j: i + j, position_t, _moves_mapping[move]))
                elif position_h[1] == position_t[0]:
                    # same column / y : just make the same move
                    position_t = tuple(
                        map(lambda i, j: i + j, position_t, _moves_mapping[move]))
                else:
                    # we need to move diagonally
                    if need_to_move_horizontally:
                        position_t = (
                            position_t[0]+_moves_mapping[move][0], position_h[1])
                    elif need_to_move_vertically:
                        position_t = (
                            position_h[0], position_t[1]+_moves_mapping[move][1])

            # we make a copy of the tupble
            trail.add(position_t+tuple())

            steps -= 1
    # ordered = list(dict.fromkeys(trail))
    # print("Trail size {}".format(len(trail)))
    print("Trail size no duplicates {}".format(len(trail)))
    return len(trail)


def load_data(textfile) -> list:
    data_raw = [list(line.split()) for line in open(
        textfile).read().strip().splitlines()]
    move_set = []
    for direction, steps in data_raw:
        # print("Direction: {}, Steps: {}".format(direction, steps))
        move_set.append((direction, int(steps)))
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
