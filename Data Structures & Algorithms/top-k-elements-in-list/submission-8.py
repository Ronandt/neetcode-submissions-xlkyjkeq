class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_list = {}
        bucket_sort = [[] for x in range(len(nums))]
        res = []
        for x in nums:
            if x not in freq_list:
                freq_list[x] = 0
            else:
                freq_list[x] += 1
        for x, y in freq_list.items():
            
            bucket_sort[y].append(x)
        print(bucket_sort)
        for x in range(len(bucket_sort)-1, -1, -1):
            print(len(res)-1, k)

            for y in bucket_sort[x]:
                print(res, k)
                if len(res) == k:
                    break
                res.append(y)

        

        return res

  