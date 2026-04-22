class Solution:
    def findMin(self, nums: List[int]) -> int:
        pointer_1 = 0
        #[1,2,3,4,0]
        #0,1,2,3,4
        pointer_2 = len(nums) - 1
        result =nums[0]
        while pointer_1 <= pointer_2:
            if nums[pointer_1] <= nums[pointer_2]:
                return nums[pointer_1]
            m = (pointer_1 + pointer_2)//2
            m_val = nums[m]
            result = min(result, m_val)
            if m_val >= nums[pointer_1]:
                pointer_1 = m + 1
            else:
                pointer_2 = m 

        return result
            


            