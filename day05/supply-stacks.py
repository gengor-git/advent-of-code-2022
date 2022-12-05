from queue import LifoQueue
import re

input_file = "./day05/input.txt"


def clean(source : str):
    #[\[\]]|[ ]{4}
    return_value = re.sub(r"[\[\]]", "", source)
    return_value = re.sub(r"[\ ]{12}", " # # #", return_value)
    return_value = re.sub(r"[\ ]{9}", " # # ", return_value)
    return_value = re.sub(r"[\ ]{5}", " # ", return_value)
    return_value = re.sub(r"[\ ]{4}", " #", return_value)
    print("Changing '{}' to '{}'.".format(source, return_value))
    return return_value


def part1():
    data = open(input_file).read().split("\n")

    stack_strings = data[0:9]
    moves = data[11:-1]

    result = ""

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
    return result


if __name__ == "__main__":
    print(part1())

