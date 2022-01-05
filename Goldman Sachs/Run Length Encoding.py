# Question-4

#Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
#eg: if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
#You are required to complete the function encode that takes only one argument the string which is to be encoded & returns 
#the encoded string.

#Your task is to complete this function, Function should return complete string
def encode(arr):
    # Code Starts here
    l = ''
    j=0
    while j<len(arr):
        count = 0
        c = arr[j]
        j = j+1
        while j<len(arr) and c==arr[j]:
            count +=1
            j=j+1
        l=l+c+str(1+count)    
    return l    
    # code ends here 
    
    
#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends