n=input("patient:")
a,b,c,d,e=map(float,input("temperatures").split())
m=max(a,b,c,d,e)
mi=min(a,b,c,d,e)
r=0
for i in a,b,c,d,e:
  if i>100:
    r+=1
print(m)
print(mi)
print(r)    
