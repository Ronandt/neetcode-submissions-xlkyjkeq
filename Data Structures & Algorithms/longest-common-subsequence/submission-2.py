class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        column = len(text2)
        matrix = [[0 ]* column for x in range(row)]
        print(matrix)
        for row_index in range( row-1, -1, -1):
         
            for column_index in range(column-1, -1, -1):
                if text1[row_index] == text2[column_index]:
                    matrix[row_index][column_index] = 1
                    if row_index+1 in range(row) and column_index+1 in range(column):
                        matrix[row_index][column_index] += matrix[row_index +1][column_index + 1]
                else:
                    res_1 = 0
                    res_2 = 0
                    if row_index + 1 in range(row):
                        res_1 = matrix[row_index + 1][column_index]
                    if column_index + 1 in range(column):
                        res_2 = matrix[row_index][column_index + 1]
                    matrix[row_index][column_index] = max(res_1, res_2)

        print(matrix)       
        
        return matrix[0][0]