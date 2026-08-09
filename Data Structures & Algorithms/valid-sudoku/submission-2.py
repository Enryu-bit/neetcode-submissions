from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid=0
        for i in range(len(board[0])):
            mapr=defaultdict(int)
            mapc=defaultdict(int)
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    mapr[board[i][j]]+=1
                    if mapr[board[i][j]]>1:
                        return False
                if board[j][i] != ".":
                    mapc[board[j][i]]+=1
                    if mapc[board[j][i]]>1:
                        return False
        for k in range(0,9,3):
            for l in range(0,9,3):
                map1=defaultdict(int)
                b1=[row[l:l+3] for row in board[k:k+3]]
                for i in range(0,3):
                    for j in range(0,3):
                        if b1[i][j] == 0:
                            return False
                        if b1[i][j] != ".":
                            map1[b1[i][j]]+=1
                            if map1[b1[i][j]]>1:
                                return False
        return True      
        



