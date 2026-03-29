class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maximum = float("-inf")
        current = 0
        for x in nums:
            if(current + x < 0):
                current = 0
            else:
                current+= x
                maximum = max(current, maximum)
        if current <= 0:
            return max(nums)
        return int(maximum)
