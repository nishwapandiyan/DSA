class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        def is_valid(board, row, col):
            # Check the column strictly above the current row
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check the upper-left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Check the upper-right diagonal
            i, j = row, col
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def solve(board, row):
            # Base Case: All queens are successfully placed
            if row == n:
                # Format the board and add to results
                result.append(["".join(r) for r in board])
                return

            # Try placing a queen in every column of the current row
            for col in range(n):
                if is_valid(board, row, col):
                    # Place the queen
                    board[row][col] = "Q"
                    
                    # Explore further
                    solve(board, row + 1)
                    
                    # Backtrack: Remove the queen to try the next configuration
                    board[row][col] = "."

        # Initialize an empty N x N board
        board = [["." for _ in range(n)] for _ in range(n)]
        solve(board, 0)

        return result