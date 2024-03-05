class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins: # Fisrtly traverse the object
            for j in range(coin, amount+1): # Then Traverse the bag
                dp[j] += dp[j-coin] # dp holds the combination
            print(dp)
        
        return dp[-1]
        '''
        print("------------------")
        dp = [0] * (amount+1)
        dp[0] = 1
        for j in range(0, amount+1): # Fisrtly traverse the bag
            for coin in coins: # Then traverse the object
                dp[j] += dp[j-coin]
            print(dp) # dp holds the permutations
        '''

