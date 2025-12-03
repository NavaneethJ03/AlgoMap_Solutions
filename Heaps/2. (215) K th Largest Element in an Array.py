# Brute Force Solution 
class Solution:
	def Kthelement(self , nums:List[int]) -> int:
		nums.sort()
		return nums[len(nums) - k]
# Time Complexity - O(N Log N)
# Space Complexity - O(1)

# Using Max Heap 

class Solution:
	def Kthelement(self , nums: List[int]) -> int:
		heap = [-num for num in nums]
		heapq.heapify(heap)
		res = 0 
		for i in range(k):
			res = heapq.heappop(heap)
		return res
# Time Complexity - O(N + K log N) 
"""The above is due to the fact that the heapify method takes O(n) time and then
	the pop operation takes place 'k' times and for each time it takes a time complexity of Log n """
# Space Complexity - O(N) Since we use the heap to store n elements 

# Using Min Heap 

class Solution:
	def Kthelement(self , nums: List[int]) -> int:
		min_heap = []
		for i in range(len(nums)):
			if len(min_heap) < k:
				heapq.heappush(heap , nums[i])
			else:
				heapq.heappushpop(heap , nums[i])
		return min_heap[0]
# Time Complexity - O(N log K)
""" This is due to fact that the nums array is parsed n times and also with each parsing either a push or both 
	push pop occurs which takes a time of log k each so it results to the N Log K .
"""
# Space Complexity - O(K) since the max size of the heap is k 
