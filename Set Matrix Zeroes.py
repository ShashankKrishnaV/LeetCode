class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=[]
        c=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    c.append(j)
                    r.append(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i in r) or (j in c):
                    matrix[i][j]=0
                    
