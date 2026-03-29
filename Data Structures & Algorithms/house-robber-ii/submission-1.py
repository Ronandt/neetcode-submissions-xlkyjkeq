class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:len(nums)-1]))
    
    def helper(self, nums):
        if len(nums) <= 2:
            return max(nums)
        one = nums[0]
        two = max(nums[0], nums[1])
        for x in range(2, len(nums)):
            maximum = max(one + nums[x], two)
            one = two
            two = maximum
        return max(one,two )
