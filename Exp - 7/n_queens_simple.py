print("Enter the number of queens")
N = int(input())

board = [[0] * N for _ in range(N)]

def attack(i, j):
    for k in range(N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(N):
        for l in range(N):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True

    return False

def N_queens(n):
    if n == 0:
        return True

    for i in range(N):
        for j in range(N):
            if not attack(i, j) and board[i][j] != 1:
                board[i][j] = 1

                if N_queens(n - 1):
                    return True

                board[i][j] = 0

    return False

if N_queens(N):
    for row in board:
        print(row)
else:
    print("No solution exists")
