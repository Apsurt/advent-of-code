import aoc
import numpy as np

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 5, 2)

def is_overlap(a,b,c,d) -> bool:
    # Architecture:
    # A = [a,b]
    # B = [c,d]
    # Truth:
    # a <= b
    assert a <= b
    # c <= d
    assert c <= d
    # Assumptions:
    # a <= c
    assert a <= c
    # Consequences:
    # a <= c <=d
    assert a <= c and a <= d
    # a <= b <= c <= d    A ⋂ B = ∅ ⇒ False
    # a <= c <= b <= d    A ⋂ B ≠ ∅ ⇒ True
    # a <= c <= d <= b    B ⊆ A ⇒ True

    # if d <= b:
    #     return True
    # if c <= b:
    #     return True
    # return False
    # Simplifies to:
    return c<=b

def solve():
    # Solve the puzzle here
    ranges, _ = aoc.Input().paragraphs().get()
    ranges = np.array(aoc.Input(ranges).lines().strip().split("-").to_int().get())
    ranges = ranges[ranges[:, 0].argsort()]

    for i in range(ranges.shape[0]-1):
        j = i+1
        # dont overlap
        # do nothing
        if not is_overlap(*ranges[i], *ranges[j]):
            continue

        # overlap
        # union -> ranges[j]
        # [0,0] -> ranges[i]
        union = [min(ranges[i,0], ranges[j,0]), max(ranges[i,1], ranges[j,1])]
        ranges[i] = 0
        ranges[j,0] = union[0]
        ranges[j,1] = union[1]
    ranges = ranges[~np.all(ranges == 0, axis=1)]

    answer = 0
    for _range in ranges:
        answer += _range[1] - _range[0] + 1

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
