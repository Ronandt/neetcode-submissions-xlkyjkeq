class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res  =[]
       
        heapq.heapify(heap)
        for x in points:
            val = (x[0]-0)**2 + (x[1]-0)**2
            heapq.heappush(heap, (val, x[0], x[1]))
        if len(heap) ==0:
            return res 
        while len(res) != k :
            popping = heapq.heappop(heap)
            print(popping)
            
            res.append([popping[1], popping[2]])
          
        
        return res 