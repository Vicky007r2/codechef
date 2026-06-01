t=int(input())
for _ in range(t):
    n=input().strip()
    sumit=sum(int(digit) for digit in n)
    print(sumit)