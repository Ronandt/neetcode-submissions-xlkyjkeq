class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1
        #-2 length
        if n == 1:
            return 1
        for x in range(n-1): 
            save = one
            one = one + two
            two = save
        return one

           

            
            