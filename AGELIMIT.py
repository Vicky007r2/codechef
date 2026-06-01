t = int(input())
for i in range(0,t):
    x,y,a = map(int,input().split())
    if a>=x and a<y:
        print("YES")
    else:
        print("NO")