class Solution:
  def fun(self , stones: List[int]) -> int:
    heap = [-stone for stone in stones] # this is the line to create a negative array to create the max heap , since python allows only min heap
    heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap , -(y-x))
        return -heap[0] if heap else 0
