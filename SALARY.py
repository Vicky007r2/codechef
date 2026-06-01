t=int(input())
for _ in range (t):
    n=int(input())
    salar=list(map(int,input().split()))
    minsalar=min(salar)
    totalsum=sum(salar)
    minmove=totalsum-(n*minsalar)
    print(minmove)