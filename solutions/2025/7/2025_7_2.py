import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 7, 2)

def solve():
    # Solve the puzzle here
    input = aoc.Input().grid()

    start_x = input.data[0].index("S")

    current_timelines = {start_x: 1}

    for y in range(input.height):
        next_timelines = {}

        for x, count in current_timelines.items():
            char = input.get(y, x)

            if char == '^':
                next_timelines[x - 1] = next_timelines.get(x - 1, 0) + count
                next_timelines[x + 1] = next_timelines.get(x + 1, 0) + count
            else:
                next_timelines[x] = next_timelines.get(x, 0) + count

        current_timelines = next_timelines

    answer = sum(current_timelines.values())
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
