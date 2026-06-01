t=int(input())
for _ in range(t):
    q,p=map(int,input().split())
    total=p*q
    if q>1000:
        total*=0.9
    print(f"{total:6f}")    