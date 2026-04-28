class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, j in enumerate(nums):
            print(j)
            if i > 0 and nums[i] == nums[i-1]: #also need to handle for the third pointer 
                    print(nums[i], nums[i-1], i, i-1)
                    continue
            first_pointer = i + 1
            second_pointer = len(nums) -1
          
            while second_pointer > first_pointer:

                res = j + nums[first_pointer] + nums[second_pointer]

                if res == 0: #do it after
                    result.append([j, nums[first_pointer], nums[second_pointer]]) 
                    while first_pointer + 1 < len(nums) and (nums[first_pointer + 1] == nums[first_pointer]):
                        first_pointer += 1

                    while second_pointer -1 >= i+1 and nums[second_pointer -1] == nums[second_pointer]:
                        second_pointer -= 1
                    
                    second_pointer -=1
                    first_pointer += 1


                if res > 0:
                    second_pointer -=1
                if res < 0:
                    first_pointer += 1

        return result


                    