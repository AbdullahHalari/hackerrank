#1


def solveMeFirst(a,b):
	# Hint: Type return a+b below
   return a+b


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

#2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


    # Write your code here

ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
sum =0
for i in ar:
    sum+=i
print(sum)
     
#3
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))
# a = [17,28,30]
# b = [99,16,8]
i = 0
alice = 0
bob = 0
while i < 3:
    if(a[i]>b[i]):
        alice+=1
    elif(a[i]<b[i]):
        bob+=1
    elif(a[i]==b[i]):
        print()
        
    i+=1
print(alice)
print(bob)
   
#4
  # Write your code here
ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
sum=0
for i in ar:
    sum+=i      
print(sum) 
    

# 5
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#



n = int(input().strip())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
    
sum = 0  
add=0
count = 0
i = 0
j=n-1
while(count<n):
    
    if(count==i):
        sum+=arr[count][i]
        add+=arr[count][j]
    count+=1
    i+=1
    j-=1

print(abs(sum-add))    

#6
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def plusMinus(arr):
    # Write your code here

# if __name__ == '__main__':
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
i=0
positive=0
negative=0
zero=0

while i < n:
    
    if(arr[i]>0):
        positive+=1
    elif(arr[i]<0):
        negative+=1
    else:
        zero+=1
        
    i+=1
print("{:.6f}".format(positive/n))
print("{:.6f}".format(negative/n))
print("{:.6f}".format(zero/n))
# plusMinus(arr)

#7
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

n = int(input().strip())

for i in range(0,n):
    for j in range(0,n):
        if(i + j >= n-1):
            print("#",end="")
        else:    
            print(" ",end="")
    print("\r")
            
#add 8
arr = list(map(int, input().rstrip().split()))
sum_min=0
sum_max=0
arr.sort()
for i in arr:
    sum_min+=i
    sum_max+=i
print(sum_min-arr[4],sum_max-arr[0])   

#add 9
candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
big=max(candles)
count=0
for i in candles:
    if(i==big):
        count+=1
        
print(count)        



    


