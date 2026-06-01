t=int(input())
for i in range (t):
    bs=int(input())
    if bs<1500:
        hra=10*bs/100
        da=90*bs/100
        gs=bs+hra+da
    else:
        hra=500
        da=98*bs/100
        gs=hra+bs+da
    print(gs)    