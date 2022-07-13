# question url - https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # have the start and end pointer for comparision      
        start, end = 0 , len(s)-1
        while start <= end:
            temp = s[end]
            s[end] = s[start]
            s[start] = temp
            
            start+=1
            end-=1
        # program is returning the s list only, we do not have to return anything
