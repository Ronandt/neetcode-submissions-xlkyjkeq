class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) -1

        while right_pointer >= left_pointer:
            average = (right_pointer+ left_pointer)//2
            average_number = nums[average]
            if average_number == target:
                return average
            #there are two sorted arrays, care about the  left and the rigfht part 
            #handle cases if right pointer greater than left and left pointer gerater than right 
            if nums[left_pointer] <= nums[average]:  # left half sorted
                # target in left?
                if nums[left_pointer] <= target < nums[average]:
                    right_pointer=average - 1
                else:
                    left_pointer = average + 1
            else:  # right half sorted
                if nums[average] < target <= nums[right_pointer]:
                    left_pointer = average + 1
                else:
                    right_pointer = average - 1

        return -1


             