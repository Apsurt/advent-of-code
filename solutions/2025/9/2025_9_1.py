import aoc
import numpy as np

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 9, 1)

def solve():
    # Solve the puzzle here
    input = aoc.Input().lines().split(",").to_int().get()

    answer = 0
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            area = (abs(input[i][0]-input[j][0])+1) * (abs(input[i][1]-input[j][1])+1)
            print(i, j, input[i], input[j], area)
            if area > answer:
                answer = area

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
