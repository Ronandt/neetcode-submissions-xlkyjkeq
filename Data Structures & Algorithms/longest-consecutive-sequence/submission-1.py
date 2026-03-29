class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seq = {

        }
        for x in range(len(nums)):
            seq[nums[x]] = nums[x] + 1
        maximum = 0
        for x in seq:
            c = x
            counters = 1
            while True:
                print(seq[c], seq)
                if seq[c] in seq:
                    counters +=1
                    c = seq[c]
                else:
                    if counters > maximum:
                        maximum = counters
                    break
        return maximum 

