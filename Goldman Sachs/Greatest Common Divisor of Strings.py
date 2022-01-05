# Question-6

#For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
#(i.e., t is concatenated with itself one or more times).
#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        r = gcd(str1,str2)
        return r

def gcd(str1, str2):
 
    # If str1 length is less than that of str2 then recur with gcd(str2, str1)
    if(len(str1) < len(str2)):
        return gcd(str2, str1)
    # If str1 is not the concatenation of str2
    elif(not str1.startswith(str2)):
        return ""
    elif(len(str2) == 0):
        # GCD string is found
        return str1
    else:
        # Cut off the common prefix part of str1 & then recur
        return gcd(str1[len(str2):], str2)       
        