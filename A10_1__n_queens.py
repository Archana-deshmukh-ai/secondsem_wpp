import random

def is_safe(board, row, col, n):
    
    for i in range(row):
        if board[i] == col:
            return False
    
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
    
    
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False
    
    return True

def solve_n_queens(n, board, row, solutions):
    if row == n:
        solutions.append(board[:])
        return
    
    available_positions = list(range(n))
    random.shuffle(available_positions)  
    
    for col in available_positions:
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, board, row + 1, solutions)
            board[row] = -1

def print_solution(board):
    n = len(board)
    for i in range(n):
        row = ['.'] * n
        row[board[i]] = 'Q'
        print(' '.join(row))
    print('\n')

def main():
    n = 8
    board = [-1] * n  
    solutions = []
    solve_n_queens(n, board, 0, solutions)
    
    if solutions:
        print(f"Found {len(solutions)} solutions. Displaying one randomly:")
        random_solution = random.choice(solutions)
        print_solution(random_solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

