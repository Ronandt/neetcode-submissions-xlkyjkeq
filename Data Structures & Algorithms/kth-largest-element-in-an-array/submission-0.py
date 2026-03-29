class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        val = 0
        for _ in range(k):
            val = heapq.heappop(nums)
        return -val 

        