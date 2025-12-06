import aoc
import numpy as np

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 6, 1)

def solve():
    # Solve the puzzle here
    input = aoc.Input().lines().strip().split().get()
    operands = np.array(aoc.Input(input[:-1]).to_int().get())
    operators = input[-1]

    answer = 0
    for i in range(operands.shape[1]):
        if operators[i] == "+":
            answer += np.sum(operands[:,i])
        if operators[i] == "*":
            answer += np.prod(operands[:,i])

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
