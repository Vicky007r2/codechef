t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    uj=a[k-1]
    a.sort()
    print(a.index(uj)+1)