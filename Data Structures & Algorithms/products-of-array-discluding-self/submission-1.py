class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        if(len(nums) ==0):
            return []
        prefix = [nums[0]]
        postfix = [nums[-1]]
        for x in nums[1:]:
            prefix.append(prefix[-1] * x)
        nums.reverse()
        for y in nums[1:]:
            postfix.insert(0, postfix[0] * y)
        print(prefix)
        print(postfix)
        for x in range(len(nums)):
            total = 1
            if x-1 in range(len(nums)):
                total = total * prefix[x-1]
            if x + 1 in range(len(nums)):
                total = total * postfix[x + 1]
            res.append(total)
        return res

        