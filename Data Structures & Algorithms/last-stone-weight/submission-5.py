class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        if len(stones) == 1:
            return -stones[0]
        while len(stones) > 1:
            result_1 = -heapq.heappop(stones)
            result_2 = -heapq.heappop(stones)
           
            return_stone = result_1 - result_2
            print(result_1, result_2, return_stone)
            if(return_stone != 0):
                heapq.heappush(stones ,-return_stone)
        if(len(stones) == 0):
            return 0    
        return -stones[0]


            