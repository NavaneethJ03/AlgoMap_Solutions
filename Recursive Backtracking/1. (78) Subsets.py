class Solution:
    def subsets(self , nums[List[int]]) -> List[List[int]]:
        result = []
        subset = []
        def backtrack(i):
            if i >= len(nums):
                result.append(subset[:]) # result.append(subset.copy())
                return
            backtrack(i+1)
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

        backtrack(0)
        return result
