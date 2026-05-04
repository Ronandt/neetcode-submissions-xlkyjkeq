class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = {x : [] for x in range(numCourses)}
        #Add courses that are avaliabnle to you if you complete it or that is related
        #Also add in degrees to the depdenent courses (opp)
        res = []
        indegree = [0] * numCourses
        for x in prerequisites:
            pre_req[x[1]].append(x[0])
            indegree[x[0]] += 1
        
        queue = deque()
        for x in range(len(indegree)):
            if indegree[x] == 0:
                queue.append(x)
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for a in pre_req[node]:
                indegree[a] -=1
                if indegree[a] ==0:
                    queue.append(a)
        return res if len(res) == numCourses else []
            

