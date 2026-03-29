class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pointer_1 = 0
        pointer_2 = len(nums) -1
        while pointer_2 >= pointer_1:
            average = (pointer_2 + pointer_1)//2
            print(nums[average], pointer_1, pointer_2)

            if nums[average] == target:
                return average
            if target > nums[average]:
                pointer_1 = average + 1
            elif nums[average] > target:
                pointer_2 = average - 1
        print(pointer_1, pointer_2)
        return -1