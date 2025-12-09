import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 9, 2)


def is_valid(p1, p2, polygon) -> bool:
    rx_min = min(p1[0], p2[0])
    rx_max = max(p1[0], p2[0])
    ry_min = min(p1[1], p2[1])
    ry_max = max(p1[1], p2[1])

    n = len(polygon)
    for k in range(n):
        u = polygon[k]
        v = polygon[(k + 1) % n]

        ex_min, ex_max = min(u[0], v[0]), max(u[0], v[0])
        ey_min, ey_max = min(u[1], v[1]), max(u[1], v[1])

        is_vertical = (ex_min == ex_max)

        if is_vertical:
            if rx_min < ex_min < rx_max:
                overlap_start = max(ey_min, ry_min)
                overlap_end = min(ey_max, ry_max)
                if overlap_end > overlap_start:
                    return False
        else:
            if ry_min < ey_min < ry_max:
                overlap_start = max(ex_min, rx_min)
                overlap_end = min(ex_max, rx_max)
                if overlap_end > overlap_start:
                    return False

    cx = (p1[0] + p2[0]) / 2.0
    cy = (p1[1] + p2[1]) / 2.0

    inside = False
    for k in range(n):
        u = polygon[k]
        v = polygon[(k + 1) % n]

        if (v[1] > cy) != (u[1] > cy):
            idx = (v[0] - u[0]) * (cy - u[1]) / (v[1] - u[1]) + u[0]
            if idx > cx:
                inside = not inside

    return inside

def solve():
    # Solve the puzzle here
    polygon = aoc.Input().lines().split(",").to_int().get()
    n = len(polygon)

    answer = 0
    for i in range(n-1):
        for j in range(i+1, n):
            width = abs(polygon[i][0] - polygon[j][0]) + 1
            height = abs(polygon[i][1] - polygon[j][1]) + 1
            area = width * height
            if area > answer:
                if is_valid(polygon[i], polygon[j], polygon):
                    answer = area

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
