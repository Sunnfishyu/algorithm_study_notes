# import numpy as np
# res = []
# def solveNQueens(n):
    
#     board = np.full((n,n),".")
#     backtrack(board, 0)
#     return res

# def backtrack(board, row):
    
#     n=len(board)
#     if row == n:
#         print("board")
#         print(board)
#         res.append(board)
#         print("res")
#         print(res)
#         return res
    
#     for col in range(n):
#         # prune invalid selections
#         if not isValid(board, row, col):
#             continue
#         # add to path
#         board[row][col] = 'Q'
#         # next selection
#         backtrack(board, row+1)
#         # deselect from path
#         board[row][col] = '.'
        
# def isValid(board, row, col):
#         n = len(board)
#         # check same column
#         for i in range(n):
#             if board[i][col] == 'Q':
#                 return False
#         # check same diagonal
#         i = row - 1
#         j = col + 1
#         while i >= 0 and j < n:
#             if board[i][j] == 'Q':
#                 return False
#             i-=1
#             j+=1
#         return True


# final=solveNQueens(3)
# print("final")
# print(final)


class Solution:
    res = []
    
    def solveNQueens(self, n: int):
        board = [['.' for x in range(n)] for y in range(n)]
        self.backtrack(board, 0)
        return self.res
    
    def backtrack(self, board, row):
        
        n=len(board)
        if row == n:
            self.res.append(board)
            return self.res
        
        for col in range(n):
            # prune invalid selections
            if not self.isValid(board, row, col):
                continue
            # add to path
            board[row][col] = 'Q'
            # next selection
            self.backtrack(board, row+1)
            # deselect from path
            board[row][col] = '.'
            
    def isValid(self, board, row, col):
            n = len(board)
            # check same column
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            # check same diagonal
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            return True

sol=Solution()
print(sol.solveNQueens(3))