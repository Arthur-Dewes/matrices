def get_main_diagonal(grid: list[list[int]]) -> list[list[int]]:
    return [grid[i][i] for i in range(len(grid))]


def get_secondary_diagonal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    return [grid[i][n - 1 - i] for i in range(n)]


def zero_outside_main_diagonal(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    new_grid = [[grid[i][j] if i == j else 0 for j in range(n)] for i in range(n)]
    return new_grid


def reverse_grid(grid: list[list[int]]) -> list[list[int]]:
    n = len(grid)
    return [grid[i][::-1] for i in range(n - 1, -1, -1)]

def min_path_sum(grid: list[list[int]]) -> int:
    """Calculates the minimum cost to traverse a matrix from the top-left corner to the bottom-right corner. 
    Movement is restricted to right or downward directions only."""
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the array with infinite values
    res = [float('inf')] * cols
    res[0] = grid[0][0]

    for c in range(1, cols):
        res[c] = res[c-1] + grid[0][c]

    for r in range(1, rows):
        res[0] += grid[r][0]

        for c in range(1, cols):
            res[c] = min(res[c], res[c-1]) + grid[r][c]

    return res[cols-1]
