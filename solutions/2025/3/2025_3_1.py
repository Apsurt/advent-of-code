import aoc
import numpy as np

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 3, 1)

def solve():
    # Solve the puzzle here
    input = aoc.Input().lines().strip().map(list).to_int().get()
    answer = 0
    for line in input:
        idx1 = np.argmax(line[:-1])
        idx2 = np.argmax(line[idx1+1:])
        answer += (10*line[idx1]) + line[idx2+idx1+1]
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
