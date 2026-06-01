n=int(input())
weapons=list(map(int,input().split()))
evens=0
odds=0
for w in weapons:
    if w%2==0:
        evens+=1
    else:
        odds+=1
if evens>odds:
    print("READY FOR BATTLE")
else:
    print("NOT READY")