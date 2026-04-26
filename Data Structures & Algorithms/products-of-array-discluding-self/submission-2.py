class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = [nums[-1]]
        res = []
        for x in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[x])

        for x in range(len(nums) -2, -1, -1):
            postfix.insert(0, postfix[0] * nums[x])
        for x in range(len(nums)):
            pre = 1
            post = 1
            if (x-1) >= 0:
                pre =prefix[x-1]
            if (x+ 1) < len(nums):
                post = postfix[x + 1] 
            res.append(pre * post)
            
        return res
