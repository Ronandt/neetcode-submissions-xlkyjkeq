class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = len(nums) -1
        while current != 0:
            reach = current - 1

            while reach != -1:
                if nums[reach] >= current-reach:
                    current = reach
                    break
                else:
                    reach -=1
            else:
                return False
        return True
            

