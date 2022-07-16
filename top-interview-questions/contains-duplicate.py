# question url - https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return will be true, when raw list len is not equals to unique elements of list, else when equals than false 
        return len(nums) != len(set(nums))
