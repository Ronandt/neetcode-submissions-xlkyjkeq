class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates = list(sorted(candidates))
        def dfs(index):
            if target == sum(subset):
                res.append(subset.copy())
                return
            if index >= len(candidates) or sum(subset) > target:
                return
           

            
            subset.append(candidates[index])
        

            dfs(index + 1)
            subset.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1)
        dfs(0)
        return res