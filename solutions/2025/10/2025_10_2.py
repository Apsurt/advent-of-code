import aoc
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 10, 2)

def solve():
    input_data = aoc.Input().lines().strip().split().get()
    answer = 0

    for line in input_data:
        targets = np.array(list(map(int, line[-1][1:-1].split(","))), dtype=float)

        raw_buttons = line[1:-1]
        rows = len(targets)
        cols = len(raw_buttons)
        A = np.zeros((rows, cols))

        for col_idx, btn_str in enumerate(raw_buttons):
            affected_indices = map(int, btn_str[1:-1].split(","))
            for row_idx in affected_indices:
                if row_idx < rows:
                    A[row_idx, col_idx] = 1

        c = np.ones(cols)

        constraints = LinearConstraint(A, lb=targets, ub=targets)

        integrality = np.ones(cols)

        bounds = Bounds(lb=0, ub=np.inf)

        res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

        if res.success:
            presses = np.round(res.x)
            answer += int(np.sum(presses))
        else:
            pass

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
