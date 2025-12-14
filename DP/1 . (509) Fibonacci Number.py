class Solution:
    def fib(self , n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        f1 = 0 
        f2 = 1
        summ = f1 + f2
        for i in range(2 , n+1):
            summ = f1 + f2 
            f1 = f2 
            f2 = summ 

        return summ 

# Time Complexity - O(N) 
# Space Complexity - O(1) 

# Top - Down DP (Memoization)

class Solution:
    def fib(self , n:int) -> int:
        dp = [n+1] * 0
        dp[0] , dp[1] = 0 , 1
        for i in range(2 , n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
# Time Complexity - O(N)
# Space Complexity - O(N)

# Bottom - Up DP (Tabulation) 

class Solution:
    def fib(self , n: int) -> int:
        memo = {0:0 , 1:1}
        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]
        return f(n)

# Time Complexity - O(N)  
# Space Complexity - O(N)
