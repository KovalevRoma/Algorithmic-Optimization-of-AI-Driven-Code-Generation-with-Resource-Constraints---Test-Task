import numpy as np
import math

def generate_initial_matrix(n, m):
    matrix = np.zeros((n, m))
    matrix[n - 1, 0] = 1
    return matrix

def get_transition_matrix(n, m, current_matrix):
    """
    Generates the next state of the matrix by applying transition rules. 
    Each element is updated as the average of its four neighbors, considering 
    periodic boundary conditions (wrapping around the edges of the matrix).
    """
    transition_matrix = np.zeros((n, m))

    def get_value(i, j):
        return current_matrix[(i+n)%n, (j+m)%m]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i, j + 1) + get_value(i + 1, j) + get_value(n - 1, j) + get_value(i, m - 1)
                )
            elif i == 0 and j == m - 1:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i, j - 1) + get_value(i + 1, j) + get_value(n - 1, j) + get_value(0, 0)
                )
            elif i == n - 1 and j == 0:
                transition_matrix[i, j] = 0.25 * (
                    get_value(0, 0) + get_value(i, j + 1) + get_value(i - 1, j) + get_value(i, m - 1)
                )
            elif i == n - 1 and j == m - 1:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i, j - 1) + get_value(i - 1, j) + get_value(i, 0) + get_value(0, m - 1)
                )
            elif i == 0 and 1 <= j <= m - 2:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i, j - 1) + get_value(i, j + 1) + get_value(i + 1, j) + get_value(n - 1, j)
                )
            elif i == n - 1 and 1 <= j <= m - 2:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i, j - 1) + get_value(i, j + 1) + get_value(i - 1, j) + get_value(0, j)
                )
            elif j == 0 and 1 <= i <= n - 2:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i - 1, j) + get_value(i + 1, j) + get_value(i, j + 1) + get_value(i, m - 1)
                )
            elif j == m - 1 and 1 <= i <= n - 2:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i - 1, j) + get_value(i + 1, j) + get_value(i, j - 1) + get_value(i, 0)
                )
            else:
                transition_matrix[i, j] = 0.25 * (
                    get_value(i - 1, j) + get_value(i + 1, j) + get_value(i, j - 1) + get_value(i, j + 1)
                )

    return transition_matrix

def print_matrix(matrix):
    print("\n".join([" ".join([f"{val:.6f}" for val in row]) for row in matrix]))

def main():
    n, m = map(int, input("Enter the dimensions of the matrix (n m): ").split())
    initial_matrix = generate_initial_matrix(n, m)

    transition_matrix = initial_matrix
    for _ in range(n*m*int(math.log(n*m))):
        transition_matrix = get_transition_matrix(n, m, transition_matrix)

    print(f"Matrix of possibilities after {n*m} iterations:")
    print_matrix(transition_matrix)

if __name__ == "__main__":
    main()
