import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 1, 1)

def solve():
    # Solve the puzzle here
    input = aoc.Input().lines().map(lambda x: int(x.replace("L", "-").replace("R", ""))).get()
    answer = 0
    position = 50
    for num in input:
        position += num
        position %= 100
        if position == 0:
            answer += 1
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
