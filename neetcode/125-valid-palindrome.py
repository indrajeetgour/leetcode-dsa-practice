## problem url - https://leetcode.com/problems/ /

class Solution:
    def isPalindrome(self, s: str) -> bool:
        all_alnum = ''.join(element for element in s if element.isalnum()).lower()
        
        start = 0
        end = len(all_alnum) - 1
        
        while start < end:
            if all_alnum[start] != all_alnum[end]:
                return False
            start +=1
            end -=1
        
        return True 
