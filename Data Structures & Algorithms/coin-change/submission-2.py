class Solution:
    #[2,3] #7
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = [float("inf")] * (amount + 1)
        total[0] = 0
        for x in range(1, len(total)):
            for c in coins:
                remainder = x-c
                if(remainder < 0):
                    continue
                number = total[remainder] + 1
                if total[x] > number:
                    total[x] = number
        if total[-1] == float("inf"):
            return -1
        return int(total[-1])

             