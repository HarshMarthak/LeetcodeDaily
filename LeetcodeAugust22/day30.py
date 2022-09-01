class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top=0
        bottom=len(matrix)-1
        while top<=bottom:
            matrix[top],matrix[bottom]=matrix[bottom],matrix[top]
            top+=1
            bottom-=1
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        
