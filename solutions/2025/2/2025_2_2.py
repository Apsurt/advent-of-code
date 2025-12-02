from functools import lru_cache
import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 2, 2)

@lru_cache
def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

@lru_cache
def is_valid(num: int) -> bool:
    num = str(num)
    half = len(num)//2
    for length in range(1, half+1):
        if len(set(chunkstring(num, length))) == 1:
            return True
    return False

def solve():
    # Solve the puzzle here
    input = aoc.Input().strip().split(",").split("-").to_int().get()
    answer = 0
    for id_range in input:
        print(id_range)
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
