import aoc
import numpy as np
import itertools

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 10, 1)

def is_valid(buttons, target):
    lights = [0]*len(target)

    for button in buttons:
        for light_to_switch in button:
            lights[light_to_switch] = abs(lights[light_to_switch]-1)

    return lights == target

def solve():
    # Solve the puzzle here
    input = aoc.Input().lines().strip().split().get()
    answer = 0
    for i in range(len(input)):
        lights = [1 if light=="#" else 0 for light in input[i][0][1:-1]]
        buttons = [list(map(int, button[1:-1].split(","))) for button in input[i][1:-1]]

        combinations = np.array(list(itertools.product([0,1], repeat=len(buttons))))
        #sort from least to most 1s
        combinations = combinations[np.argsort(combinations.sum(axis=1), kind='stable')][1:]
        for combination in combinations:
            if is_valid([buttons[i] for i in np.where(combination==1)[0]], lights):
                answer += np.sum(combination)
                break

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
