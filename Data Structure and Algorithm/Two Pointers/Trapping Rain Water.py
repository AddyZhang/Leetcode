class Solution:
    def trap(self, height: List[int]) -> int:
        """
        trap += min(left_high, right_high) - own bar
        """
        # Make a left highest list
        left_highest = [0]*(len(height)+1)
        # left_highest[0] = 0
        for i,x in enumerate(height):
            left_highest[i+1] = max(x,left_highest[i])
        print (left_highest)
        
        # right_highest = [0] * (len(height)+1)
        
        trap = 0
        right_highest = 0
        for i in range(len(height)-1,-1,-1):
            right_highest = max(height[i], right_highest)
            trap += max(min(left_highest[i],right_highest) - height[i], 0)
        
        return trap
