import aoc
import numpy as np

# Set your Advent of Code context
YEAR, DAY, PART = (2025, 8, 1)

def solve():
    # Solve the puzzle here
    input = np.array(aoc.Input().lines().strip().split(",").to_int().get())

    vectors = input
    ids = np.arange(vectors.shape[0])

    idx_1, idx_2 = np.triu_indices(len(ids), k=1)
    pairs = np.column_stack((ids[idx_1], ids[idx_2]))
    vector_pairs = vectors[pairs]

    distances = np.sqrt(np.sum(np.pow(vector_pairs[:,0]-vector_pairs[:,1],2), axis=1))
    sorted_pairs = pairs[np.argsort(distances)]

    final_connections = sorted_pairs[:1000]

    A = np.zeros((vectors.shape[0], vectors.shape[0]), dtype=int)
    rows = final_connections[:, 0]
    cols = final_connections[:, 1]
    A[rows, cols] = 1
    A[cols, rows] = 1

    degrees = np.sum(A, axis=1)
    D = np.diag(degrees)
    L = D - A

    eigenvalues, eigenvectors = np.linalg.eigh(L)
    null_eigen_idx = np.where(eigenvalues < 1e-10)[0]
    rounded_vectors = np.round(eigenvectors[:, null_eigen_idx], decimals=8)

    _, unique_counts = np.unique(rounded_vectors, axis=0, return_counts=True)

    answer = np.prod(np.sort(unique_counts)[::-1][:3])
    return answer

def main():
    answer = solve()
    print(answer)
    # Uncomment line below when you're ready to submit
    aoc.submit(answer)

if __name__ == "__main__":
    main()
