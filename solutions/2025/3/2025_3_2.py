import aoc
import numpy as np

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 3, 2)

def solve():
    # Solve the puzzle here
    n = 12
    input = aoc.Input().lines().strip().map(list).to_int().map(np.array).get()
    answer = 0
    for line in input:
        # print(line)
        idx = [-1]
        # print("segment", line[:1-n])
        idx.append(int(np.argmax(line[:1-n])))
        while len(idx[1:]) < 12:
            offset = 1+idx[-1]
            skipped = np.sum(np.diff(idx))-(len(idx)-1)
            constraint = (len(line)-n+1)-skipped
            # print(np.diff(idx))
            # print("skipped", skipped, "offset", offset, "constraint", constraint)
            # print("segment", line[offset:offset+constraint], "idx", idx)
            idx.append(offset+int(np.argmax(line[offset:offset+constraint])))
        # print(line[idx[1:]])
        # print()
        answer += int("".join(map(str,line[idx[1:]])))
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
