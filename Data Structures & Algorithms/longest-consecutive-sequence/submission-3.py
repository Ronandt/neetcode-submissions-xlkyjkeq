class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for x in nums:
            val = 1
            if x - 1 not in nums:
                
                while  x+val in nums:
                    val +=1
            best = max(best, val)
        return best
                    
