n=input()
a,b,c,d=map(int,input().split())
total=a+b+c+d
m=max(a,b,c,d)
print(total)
print(m)
if total>5000:
  discount=total*15/100
  print(discount)
