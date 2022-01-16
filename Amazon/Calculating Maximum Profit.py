# Question-1

#In the stock market, a person buys a stock and sells it on some future date.
#Given the stock prices of N days in an array A[ ] and a positive integer K, 
#find out the maximum profit a person can make in at-most K transactions. 
#A transaction is equivalent to (buying + selling) of a stock and new transaction 
#can start only when the previous transaction has been completed.



class Solution:
    def maxProfit(self, K, N, A):

        # Table to store results of subproblems profit[t][i] stores maximum profit 
        # using atmost t transactions up to day i (including day i) 
        n     = N
        k     = K
        price = A
        profit = [[0 for i in range(n + 1)] 
                     for j in range(k + 1)] 

        # Fill the table in bottom-up fashion 
        for i in range(1, k + 1): 
            prevDiff = float('-inf')
            for j in range(1, n): 
                prevDiff     = max(prevDiff, profit[i - 1][j - 1] - price[j - 1]) 
                profit[i][j] = max(profit[i][j - 1], price[j] + prevDiff) 
        return profit[k][n - 1] 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends