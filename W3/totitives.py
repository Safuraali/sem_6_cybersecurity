import math
n=int(input("enter a number:"))
count=0
for i in range(1,n):
  if math.gcd(i,n)==1:
      count+=1
      print(i)
print("eulers totient",count)
