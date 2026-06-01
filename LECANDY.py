t=int(input())
for _ in range (t):
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    total=sum(a)
    if total<=c:
        print("Yes")
    else:
        print("No")