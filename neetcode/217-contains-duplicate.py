# url - https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        matrics_dic = {}
        
        # creating the dic with ele and its value as its occurence value
        for ele in nums:
            matrics_dic[ele] = matrics_dic.get(ele,0) + 1
        
        # checking the value of ele in dic having value more than 1
        for key, value in matrics_dic.items():
            if value > 1:
                return True
            
        return False
            
        
