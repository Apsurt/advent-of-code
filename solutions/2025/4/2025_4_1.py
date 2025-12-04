import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 4, 1)

def solve():
    # Solve the puzzle here
    grid = aoc.Input().grid()
    answer = 0

    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(y,x) != "@":
                continue
            neighbours = grid.neighbors(y,x, diagonals=True).values()
            count = 0
            for cell in neighbours:
                if cell == "@":
                    count += 1
                if count >= 4:
                    break
            if count < 4:
                answer += 1

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
