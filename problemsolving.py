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
    


