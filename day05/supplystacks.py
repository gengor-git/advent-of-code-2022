from queue import LifoQueue
import re

def clean(source : str) -> str:
    #[\[\]]|[ ]{4}
    return_value = re.sub(r"[\[\]]", "", source)
    return_value = re.sub(r"[\ ]{12}", " # # #", return_value)
    return_value = re.sub(r"[\ ]{9}", " # # ", return_value)
    return_value = re.sub(r"[\ ]{5}", " # ", return_value)
    return_value = re.sub(r"[\ ]{4}", " #", return_value)
    print("Changing '{}' to '{}'.".format(source, return_value))
    return return_value


input_file = "./day05/input.txt"

data = open(input_file).read().split("\n")

stack_strings = data[0:9]
moves = data[10:-1]


def build_stacks() -> list:
    stack1 = LifoQueue()
    stack2 = LifoQueue()
    stack3 = LifoQueue()
    stack4 = LifoQueue()
    stack5 = LifoQueue()
    stack6 = LifoQueue()
    stack7 = LifoQueue()
    stack8 = LifoQueue()
    stack9 = LifoQueue()

    all_stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

    # going through the stacks bottom to top
    # bottom is higher numbers, top is 0
    for layer in range(7, -1, -1):
        layer_data = clean(str(stack_strings[layer])).split(" ")
        if len(layer_data) > 9:
            print("ERROR -> Box line to long with {} entries.".format(len(layer_data)))
            break
        print(layer_data)
        for current_stack in range(0,9):
            if layer_data[current_stack] != "#":
                print("Stack {} has letter {}".format(current_stack+1,layer_data[current_stack]))
                all_stacks[current_stack].put(layer_data[current_stack])
            else:
                print("No box for stack {}".format(current_stack+1))
    for i in range(0,9):
        print("Stack No. {} has {} elements.".format(i+1, all_stacks[i].qsize()))

    return all_stacks


def part1() -> str:
    result = ""
    all_stacks = build_stacks()

    # let's parse the movement data
    for move in moves:
        x = move.split()
        amount = int(x[1])
        source_stack = int(x[3])-1
        target_stack = int(x[5])-1
        print("Moving '{}' crates from '{}' to '{}'.".format(amount,source_stack+1, target_stack+1))
        for _ in range(amount):
            all_stacks[target_stack].put(all_stacks[source_stack].get())

    for i in range(0,9):
        print("Stack No. {} now has {} elements.".format(i+1, all_stacks[i].qsize()))

    for i in range(0,9):
        result += all_stacks[i].get()

    return result


def part2() -> str:
    result = ""
    all_stacks = build_stacks()

    # let's parse the movement data
    for move in moves:
        x = move.split()
        amount = int(x[1])
        source_stack = int(x[3])-1
        target_stack = int(x[5])-1
        tmp_stack = LifoQueue(maxsize=amount)
        print("Moving '{}' crates from '{}' to '{}'.".format(amount,source_stack+1, target_stack+1))
        for _ in range(amount):
            tmp_stack.put(all_stacks[source_stack].get())

        for _ in range(tmp_stack.qsize()):
            all_stacks[target_stack].put(tmp_stack.get())

    for i in range(0,9):
        print("Stack No. {} now has {} elements.".format(i+1, all_stacks[i].qsize()))

    for i in range(0,9):
        result += all_stacks[i].get()

    return result


if __name__ == "__main__":
    print("Part 1 ??? Crates on top: {}.".format(part1()))
    print("Part 2 ??? Crates on top: {}.".format(part2()))

