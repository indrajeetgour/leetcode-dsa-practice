# url - https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#       below will also not work, as it does not check for each set which the same char or not just check the len of set is same
#         first_set = set()
#         sec_set = set()
        
#         if len(s) == len(t):
#             for first_str, sec_str in zip(s,t):
#                 first_set.add(first_str)
#                 sec_set.add(sec_str)
#         if len(sec_set) == len(sec_set):
#             return True
#         return False 
        first_dic,sec_dic = {},{}
        # this will not work as zip loop will be terminated by any number which len is small
        # for first_str, sec_str in zip(s,t):
        #     first_dic[first_str] = first_dic.get(first_str,0) + 1 
        #     sec_dic[sec_str] = sec_dic.get(sec_str,0) + 1 
        for first_str in s:
            first_dic[first_str] = first_dic.get(first_str,0) + 1 
        for sec_str in t:
            sec_dic[sec_str] = sec_dic.get(sec_str,0) + 1 
        
        return first_dic == sec_dic
        
