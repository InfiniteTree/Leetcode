class Solution:
    def fib(self, n: int) -> int:
        # Method 1. Recursion
        '''
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)
        '''
        # Method 2. Simple iteration
        '''
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        fn_1, fn_2 = 1, 1
        for i in range(3, n+1):
            fn = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = fn
        return fn
        '''
        # Method 3. DP
        if n == 0:
            return 0
        dp = [0] * (n+1) # dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
