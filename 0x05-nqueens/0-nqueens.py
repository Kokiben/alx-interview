#!/usr/bin/python3
import sys


def print_solutions(n: int):
    """Backtracking function to find all solutions to the N queens problem."""
    solutions = []
    board = [-1] * n  # Initialize board with -1 for each row

    def is_safe(row: int, col: int) -> bool:
        """Check if a queen can be placed at board[row] = col."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(row - r):
                return False
        return True

    def solve(row: int):
        """Recursive backtracking function to find all solutions."""
        if row == n:
            # Solution found, append to solutions
            solutions.append([[i, board[i]] for i in range(n)])
        else:
            for col in range(n):
                if is_safe(row, col):
                    board[row] = col
                    solve(row + 1)
                    board[row] = -1  # Reset row position

    solve(0)
    for solution in solutions:
        print(solution)


def main():
    # Check argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate N
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(n)


if __name__ == "__main__":
    main()
