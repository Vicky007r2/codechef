n=input()
a,b,c,d,e,k=map(int,input().split())
av=(a+b+c+d+e+k)//6
count=0
m=max(a,b,c,d,e,k)
for i in a,b,c,d,e,k:
  if i<=80:
    count+=1
print(m)
print(av)    
print(count)  
