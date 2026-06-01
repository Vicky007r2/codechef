t=int(input())
for i in range(t):
    n=input()
    b=n[::-1]
    if n==b:
        print("wins")
    else:
        print("loses")