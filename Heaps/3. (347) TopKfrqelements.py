class Solution:
    def topkfrqelements(self , nums: List[int] , k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        res = []
        for key , val in count.items():
            heapq.heappush(heap , (-val , key))
        for i in range(k):
            v , k = heapq.heappop(heap)
            res.append(k)
        return res

# Time Complexity - O(N log N + K log N) ->  O(N Log N)
# Space Complexity - O(N)

class Solution:
    def topKfrqelements(self , nums: List[int] , k: int) -> List[int]:
        count = Counter(nums)
        min_heap = []
        for key , val in count.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap , (val , key))
            else:
                heapq.heappushpop(min_heap , (val , key))
        return [h[1] for h in min_heap]

# Time Complexity - O(N Log K)
# Space Complexity - O(K)
