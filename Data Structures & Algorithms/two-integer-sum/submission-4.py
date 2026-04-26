class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap_pair = {}
        for x in range(len(nums)):
            minus = target-nums[x]
            if nums[x] in hashmap_pair:
                return [ hashmap_pair[nums[x]], x]
            hashmap_pair[minus] = x
        return [67]

