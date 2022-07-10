# question - https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = []
        
        for num in range(numRows):
            # each row preparation 
            pascal_triangle_row = []
            
            # logic - to generate element of each row wise
            for row in range(num+1):
                # 1 will be the first and last element all the times
                if row == 0 or row == num:
                    # append works for both - for first and last element
                    pascal_triangle_row.append(1) 
                else:
                    # will come here only num == 2(3rd row), so by the time we try get the data from last rows using pascal_triangle[num-1][row-1], we will have the data to get, so no issues, as each row list append back to main pascal list
                    pascal_triangle_row.append(pascal_triangle[num-1][row-1] + pascal_triangle[num-1][row])
            
            # making sure each row merge/append back to main list(pascal_triangle)
            if not pascal_triangle:
                pascal_triangle = [pascal_triangle_row]
            else:
                pascal_triangle.append(pascal_triangle_row)
        
        # return the entire pascal triangle list of list
        return pascal_triangle

            
            
            
