def print_solution(board):
    """Utility function to print the board."""
    for row in board:
        print(" ".join("Q" if cell else "*" for cell in row))
    print()

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False


    return True

def solve_n_queens_util(board, col, n):
    """Utilize backtracking to solve the N Queens problem."""
    # Base case: If all queens are placed, return true
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = True
            if solve_n_queens_util(board, col + 1, n):
                return True
            board[i][col] = False  # Backtrack

    return False

def solve_n_queens(n):
    """Main function to solve the N Queens problem."""
    board = [[False] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
        return
    print_solution(board)

# Example usage
n  =  int(input("Enter size of N queens problem : "))
solve_n_queens(n)
