# question url - 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        
        while start < len(nums):
            # initial variable for value store 
            storenum1, storenum2 = None, None
            count = 0

            for num in nums[start:]:
                if storenum1 == None:
                    storenum1 = num
                    first_index = start + count
                elif (target - storenum1) == num:
                    storenum2 = num
                    sec_index = start + count
                count += 1
                    
            if storenum2 == None or storenum1 == None:
                start+=1

            elif (storenum1 + storenum2) == target:
                list_of_indices = [first_index, sec_index]

                return list_of_indices
            
            
            
