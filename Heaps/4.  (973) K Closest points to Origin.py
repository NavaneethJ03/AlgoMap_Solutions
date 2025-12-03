# Brute Force Solution 

class Solution:
    def Kclosepoints(self , points:List[List[int]] , k: int) -> List[List[int]]:
        ele = []
        for x , y in points:
            dist = x**2 + y**2
            ele.append([dist ,(x , y)])
        ele.sort(key = lambda x: x[0])
        return [p[1] for p in ele[:k]]
# Time Complexity - O(N Log N)
# Space Complexity - O(N)

# Using Min Heap 

class Solution:
    def kclosepoints(self , points:List[List[int]] , k: int) -> List[List[int]]:
        heap = []
        res = []
        for x , y in points:
            dist = x**2 + y**2
            heap.append(dist , (x , y ))
        heapq.heapify(heap)
        for i in range(k):
            d , point = heapq.heappop(heap)
            res.append(point)
        return res
# Time Complexity - O(N + K Log N)
# Space Complexity - O(N)

# Space optimized Heap solution

class Solution:
    def kclosepoints(self , points:List[List[int]] , k: int) -> List[List[int]]:
        heap = []
        for x , y in points:
            dist = x**2 + y**2
            if len(heap) < k:
                heapq.heappush(heap , (dist , (x , y)))
            else:
                heapq.heappushpop(heap , (dist , (x , y)))
        return [p[1] for p in heap]
# Time Complexity - O(N Log K)
# Space Complexity - O(K)
        
