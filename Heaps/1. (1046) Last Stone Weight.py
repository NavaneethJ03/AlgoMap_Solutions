# Brute Force solution 
class Solution:
  	def fun(self , stones: List[int] -> int:
    	while len(stones) > 1:
      		stones.sort()
      		x = stones.pop()
      		y = stones.pop()
      		if x != y:
        		stones.apppend(x - y)
    	return stones[0] if stones else 0
# Time Complexity - O( n*n  * logn) 
    # The reason being it takes n iterations of sorting which takes (n logn) hence it becomes n*n * logn.
 
# Space Complexity - O(1)

# Preferred solution using Heap
class Solution:
  	def fun(self , stones: List[int]) -> int:
    	heap = [-stone for stone in stones] 
    # this is the line to create a negative array to create the max heap,
    # since python allows only min heap
    	heapq.heapify(heap) # this function is used to convert the list to heap 
    	while len(heap) > 1:
      		y = -heapq.heappop(heap)
      		x = -heapq.heappop(heap)
      		if x != y:
        		heapq.heappush(heap , -(y-x))
   	 	return -heap[0] if heap else 0
# Time Complexity - O(n log n) n
    # It takes O(n) time for heapify and it takes about logn for push and pop in heap hence and these can occur upto n times hence
    # O(n) + O(logn ) * O(n) = O(n log n )
# Space Complexity - O(n) since we create an extra array for storing the negative values 
