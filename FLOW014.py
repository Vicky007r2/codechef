t=int(input())
for i in range(t):
    a,b,c=map(float,input().split())
    x=a>50
    y=b<0.7
    z=c>5600
    if x and y and z:
        print("10")
    elif x and y:
        print("9")
    elif y and z:
        print("8")
    elif x and z:
        print("7")
    elif x or y or z:
        print("6")
    else:
        print("5")