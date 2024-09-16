class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            new_row = [1] * (i + 1) # Create a row of 1+i length filled with 1s

            for j in range(1, i): # Calculate the values for the inner part of the row
                new_row[j] = triangle[i-1][j-1] + triangle[i-1][j]
                
            triangle.append(new_row) 
    
        return triangle

                