# Question -12


# Find total number of Squares in a N*N chessboard.

class Solution:
    def squaresInChessBoard(self, N):
         # code starts  here
         # Total number of squares in a n*n chessboard will be = ∑n2; n varying from 1 to n.
         # sum of squares of natural numbers, ∑n2 = n*((n+1)/2)*((2n+1)/3))
         
         s =round(N*((N+1)/2)*((2*N+1)/3))
         return s
         #code ends here 
         
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.squaresInChessBoard(N))
# } Driver Code Ends