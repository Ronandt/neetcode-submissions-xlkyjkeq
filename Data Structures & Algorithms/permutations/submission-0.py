class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = nums.copy()
        def dfs(index):
            if index == len(nums):
                res.append(nums.copy())
                return
      
            
            for x in range(index, len(nums)):
                nums[index], nums[x] = nums[x], nums[index]
                dfs(index + 1)
                nums[x], nums[index] = nums[index], nums[x]
           
        dfs(0)
        return res