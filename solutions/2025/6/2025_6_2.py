import aoc
from itertools import zip_longest
import math

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 6, 2)

reg = {
    "+": sum,
    "*": math.prod
}

def solve():
    with open(".aoc/cache/0160c28b/2025/inputs/day6.txt", "r") as f:
        raw_lines = f.read().splitlines()

    operands_raw = raw_lines[:-1]
    operators = raw_lines[-1].strip().split()

    grid_cols = list(zip_longest(*operands_raw, fillvalue=" "))

    transposed_operands = []
    current_group = []

    for col in grid_cols:
        col_str = "".join(col).replace(" ", "")

        if col_str:
            current_group.append(int(col_str))
        elif current_group:
            transposed_operands.append(current_group)
            current_group = []

    if current_group:
        transposed_operands.append(current_group)

    operands = transposed_operands


    answer = 0
    for i in range(len(operands)):
        answer += reg[operators[i]](operands[i])

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
