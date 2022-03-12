class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            temp = ''.join(i).replace(".",'')
            if len(set(temp))<len(temp):
                return False

        board1 = list(map(list, zip(*board)))

        for i in board1:
            temp = ''.join(i).replace(".",'')
            if len(set(temp))<len(temp):
                return False

        return True

if __name__ == "__main__":
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    print(Solution().isValidSudoku(board))