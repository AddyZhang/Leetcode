Class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, x in enumerate(nums):
            cmp = target - nums[i]
            if cmp not in dic:
                dic[x] = i
            else:
                return [dic[cmp],i]
