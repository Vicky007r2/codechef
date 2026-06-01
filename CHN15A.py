t=int(input())
for i in range (t):
    x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    count=0
    for num in arr:
        b=num+y
        if b%7==0:
           count+=1
    print(count)   