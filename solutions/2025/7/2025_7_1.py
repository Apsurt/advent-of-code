from re import L
import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 7, 1)

def solve():
    # Solve the puzzle here
    input = aoc.Input().grid()
    objects = []
    for y in range(input.height):
        for x in range(input.width):
            if input.get(y,x) == "S":
                objects.append([y,x])
                break
        if len(objects) > 0:
            break

    answer = 0
    for step in range(input.height-1):
        to_remove = []
        to_add = []
        for i in range(len(objects)):
            # move down
            objects[i][0] += 1
            obj = objects[i]

            # empty below => do nothing
            if input.get(obj[0], obj[1]) == ".":
                pass

            # splitter below => answer++  => add new to sides => remove original
            elif input.get(obj[0], obj[1]) == "^":
                answer += 1
                left,right = obj[1]-1, obj[1]+1
                if left >= 0:
                    to_add.append([obj[0], left])
                if right < input.width:
                    to_add.append([obj[0], right])
                to_remove.append(obj)

            else:
                print(input.get(obj[0], obj[1]))
                raise RuntimeError("Impossible state")

        # Remove originals
        for remove_obj in to_remove:
            objects.remove(remove_obj)
        # Add new
        for add_obj in to_add:
            if add_obj not in objects:
                objects.append(add_obj)

    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
