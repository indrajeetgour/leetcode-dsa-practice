# question url - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniq_dic = {}
        
        # iterate over given list
        for ele in nums:
            
            # dictionary preparation with key as element and value as its occurence in given list
            if ele in uniq_dic:
                uniq_dic[ele] = uniq_dic[ele] + 1
            else:
                uniq_dic[ele] = 1
                
        # for print the entire content
        # for k,v in uniq_dic.items():
        #     print(k,v)
                
        # now return the element which has 1 occurence
        for key,value in uniq_dic.items():
            if value == 1:
                return key
                
            
