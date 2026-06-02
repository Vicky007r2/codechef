n=input()
a,b,c,d,e=map(int,input().split())
av=(a+b+c+d+e)/5
count=0
m=max(a,b,c,d,e)
mi=min(a,b,c,d,e)
for i in a,b,c,d,e:
  if i>=50:
    count+=1
print(m)
print(mi)
print(av)    
print(count)    
