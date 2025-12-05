import aoc
import numpy as np

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 5, 1)

def solve():
    # Solve the puzzle here
    ranges, ingredients = aoc.Input().paragraphs().get()
    ranges = np.array(aoc.Input(ranges).lines().strip().split("-").to_int().get())
    ingredients = np.array(aoc.Input(ingredients).lines().strip().to_int().get())

    answer = 0

    # brute force
    # for ingredients -> is in any range
    for item in ingredients:
        for _range in ranges:
            if _range[0] <= item and item <= _range[1]:
                answer += 1
                break

    assert answer < len(ingredients)
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
