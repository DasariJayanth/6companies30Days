# Question-1

#Given an array of strings, return all groups of strings that are anagrams. 
#The groups must be created in order of their appearance in the original array.

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        #starts
        d = dict()
        for i in words:
            #arranging words in sorted order, making it as key so anagram words can be paired under that key
            s=''.join(sorted(i))
            #appending all the anagrams related under one key(like {key:value1,value2} pairs)
            if d.get(s,0)==0:
                d[s]=[i]
            else:
                d[s].append(i)
        ans = []
        for i in d:
            ans.append(d[i])
        return ans   
        #ends 
       
#{ 
#  Driver Code Starts
#Initial Template for Python 3 contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends