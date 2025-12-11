import aoc

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 11, 1)

def dfs(u, dest, adj, memo):
    # If destination is reached
    if u == dest:
        return 1

    # If number of paths from this node
    # is memoized
    if memo[u] != -1:
        return memo[u]

    count = 0
    for v in adj[u]:
        count += dfs(v, dest, adj, memo)

    memo[u] = count
    return count

def count_paths(edges, V, src, dest):
    adj = [[] for _ in range(V)]
    for e in edges:
        adj[e[0]].append(e[1])
    memo = [-1] * V
    return dfs(src, dest, adj, memo)

def solve():
    # Solve the puzzle here
    input = aoc.Input().lines().strip().split().get()
    labels = {}
    edges = []
    for line in input:
        if line[0][:-1] not in labels.keys():
            labels[line[0][:-1]] = len(labels)
        for i in range(1, len(line)):
            if line[i] not in labels.keys():
                labels[line[i]] = len(labels)
            new_edge = [labels[line[0][:-1]], labels[line[i]]]
            edges.append(new_edge)
    answer = count_paths(edges, len(labels), labels["you"], labels["out"])
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
