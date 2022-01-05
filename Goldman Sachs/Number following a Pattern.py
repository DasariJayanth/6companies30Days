# Question-9

#Given a pattern containing only I's and D's. I for increasing and D for decreasing.
#Devise an algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can't repeat.

class Solution:
    def printMinNumberForPattern(ob,S):
        # code starts here 
        s = ""
        i = 0
        num = 1
        if S[0] == "I":
            s += str(num)
            num += 1
        while i < len(S):
            if S[i] == "I":
                j = i
                count = 0
                while j < len(S):
                    if S[j] == "I":
                        j += 1
                        count += 1
                    else:
                        break
                for p in range(count-1):
                    s += str(num)
                    num += 1
                i = j
            elif S[i] == "D":
                j = i
                count = 0
                while j < len(S):
                    if S[j] == "D":
                        j += 1
                        count += 1
                    else:
                        break
                before = num
                num = num + count
                after = num
                while num >= before:
                    s += str(num)
                    num -= 1
                num = after+1
            i = j
        if S[-1] == "I":
            s += str(num)
        return s
        
        # code ends here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends