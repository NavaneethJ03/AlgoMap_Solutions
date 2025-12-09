class Solution:
    def combine(self , n: int , k:int ) -> List[List[int]]:
        result = [] 
        def backtrack(start , comb):
            if len(comb) == k:
                result.append(comb.copy()) # or result.append(comb[:])
                return 
            for i in range(start , n+1):
                comb.append(i)
                backtrack(i+1 , comb)
                comb.pop()

        backtrack(1 , [])
        return result


class Solution:
    def combine(self , n:int , k:int) -> List[List[int]]:
        result = []
        comb = []
        def backtrack(x):
            if len(comb) == k:
                result.append(comb[:])
            pending_left = x 
            still_need = k - len(comb)
            if pending_left > still_need:
                backtrack(x-1)
            comb.append(x)
            backtrack(x-1)
            comb.pop()

        backtrack(n)
        return result
        
            
