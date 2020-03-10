class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort the list
        lock first pointer, let second and third pointer walk to each other
        skip duplicates except zero
        """
        length = len(nums)
        target = int(0)
        result_list = []
        nums.sort()
        
        if length < 3: return result_list
        
        if all(v ==0 for v in nums): # check if is is all zero
                return [[0,0,0]]
        
        for i,num in enumerate(nums):
            j = i + 1
            k = length - 1
            if nums[i] == nums[i-1]: # check duplicates 
                i += 1
                continue
            
            while j < k:
                
                if nums[i] + nums[j] + nums[k] < target:
                    
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                        
                elif nums[i] + nums[j] + nums[k] > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1 
                else:
                    result_list.append([nums[i], nums[j], nums[k]])
                    # further explore
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            
        return result_list
     
