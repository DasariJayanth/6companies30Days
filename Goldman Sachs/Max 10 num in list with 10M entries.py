# Question-10

# Find max 10 numbers in a list having 10M entries.

def TenMaxEle(list1):  #for generalizing, #def TenMaxEle(list1,N):
    final_list = []
    for i in range(0, 10): #here in the place of 10 can repkace it with N for top N ele of list #for i in range(0,N):
        max1 = 0        
        for j in range(len(list1)):     
            if list1[j] > max1:
                max1 = list1[j]          
        list1.remove(max1)
        final_list.append(max1)
    print(final_list)

# driver code

list1 = list(map(int, input.split()))
TenMaxEle(list1) # can generalize by passing N as parameter to function #TenMaxEle(list1,N)