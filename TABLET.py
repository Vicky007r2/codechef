t=int(input())
for i in range(t):
    n,b=map(int,input().split())
    maxa=-1
    for i in range (n):
        w,h,p=map(int,input().split())
        if p<=b:
            curr=w*h
            if curr>maxa:
                maxa=curr
    if maxa==-1:
        print("no tablet")
    else:
        print(maxa)
            