class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        one = nums[-1]
        two = max(nums[-1], nums[-2]) 
        for x in range(len(nums)-3, -1, -1):
            maximum  = max(nums[x] + one, two)
            one = two 
            two = maximum
            print(maximum, two, one)
        return max(one, two)