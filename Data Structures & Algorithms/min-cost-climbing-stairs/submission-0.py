class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[-1]
        two = cost[-2] #two steps or 1 step  #anyway doesn't matter
        if len(cost) ==2:
            return min(one, two)
        total = [two, one]
        for x in range(len(cost) -2):
            current = cost[len(cost) -x -3]
            first_step = min(current+ total[1], current + total[0])
            total[-1] = total[0]
            total[0] = first_step
        return min(total)
            

            

        


