class Solution:
    def jump(self, nums: List[int]) -> int:
        #[2,4,1,1,1,1]
        #[5 or 2,4,3,2,1] #This is dp sln so this is not good
        if len(nums) == 0:
            return 0
        res = 0
        l = r = 0
        while r < len(nums) -1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res 
    