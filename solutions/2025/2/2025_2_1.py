from functools import lru_cache
import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 2, 1)

@lru_cache
def is_valid(num: int) -> bool:
    num = str(num)
    half = len(num)//2
    return num[:half] == num[half:]

def solve():
    # Solve the puzzle here
    input = aoc.Input().strip().split(",").split("-").to_int().get()
    answer = 0
    for id_range in input:
        for num in range(id_range[0], id_range[1]+1):
            answer += num if is_valid(num) else 0
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
