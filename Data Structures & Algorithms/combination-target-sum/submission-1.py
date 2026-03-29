class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(index):
            print(subset)
            if index >= len(nums) or sum(subset) > target:
                return
            if(sum(subset) == target):
                return res.append(subset.copy())
            subset.append(nums[index])
            dfs(index)
            subset.pop()

          
            dfs(index + 1)



        dfs(0)
        return res