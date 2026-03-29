class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_m = {}
        for x in nums:
            if(x in hash_m):
                return True
            hash_m[x] =1 
        return False
        