class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix)==len(matrix[0]):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i!=j and j>=i:
                        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix
        else:
            matrix2=[]
            for i in range(len(matrix[0])):
                lt=[]
                for j in range(len(matrix)):
                    lt.append(matrix[j][i])
                matrix2.append(lt)
            return matrix2
