class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix) #number of rows 
        col_len = len(matrix[0]) #number of cols 
        left = 0
        right = row_len*col_len - 1 #last element in the matrix 


        while left <= right:
            #find midpt in the matrix 
            mid = left + (right-left)//2 

            col = mid % col_len
            row = mid // col_len

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                right = mid -1
            else:
                left = mid + 1 


        
        return False 