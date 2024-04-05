class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1]:
            return False
        
        row, col = 0, 0
        while row + 1 < len(matrix) and matrix[row + 1][col] <= target:
            row += 1
        while col + 1 < len(matrix[0]) and matrix[row][col + 1] <= target:
            col += 1

        if matrix[row][col] == target:
            return True
        else:
            return False 