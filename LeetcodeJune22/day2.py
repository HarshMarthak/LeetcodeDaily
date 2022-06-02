#trivial solution

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp=[[0 for _ in range(len(matrix))] for a in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp[j][i]=matrix[i][j]
        return temp

#shortcut

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
