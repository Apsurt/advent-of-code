import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 1, 2)

def solve():
    # Solve the puzzle here
    input = aoc.Input().lines().map(lambda x: int(x.replace("L", "-").replace("R", ""))).get()
    answer = 0
    dial = 50
    for num in input:
        old = dial
        new = dial + num
        if num > 0:
            count = (new // 100) - (old // 100)
            answer += count
        elif num < 0:
            count = ((old - 1) // 100) - ((new - 1) // 100)
            answer += count
        dial = new
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
