class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = [gasses - costs for gasses, costs in zip(gas, cost)]
        total = sum(diff)
        summation = 0
        res= 0
        for x in range(len(diff)):
            summation += diff[x]
            if summation < 0:
                summation = 0
                res = x + 1
        return res
                
        