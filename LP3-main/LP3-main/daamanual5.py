21
n = int(input("Enter value of N: "))
board = [[0]*n for i in range(n)]

board[0][0] = 1

def safe(row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i in range(row):
        for j in range(n):
            if board[i][j] == 1 and abs(i-row) == abs(j-col):
                return False

    return True

def solve(row):
    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row][col] = 1

            if solve(row+1):
                return True

            board[row][col] = 0

    return False

if solve(1):
    print("N-Queens Solution:")
    for row in board:
        print(row)
else:
    print("No solution exists")
