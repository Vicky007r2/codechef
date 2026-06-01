def is_rainbow(n,arr):
    if arr!=arr[::-1]:
        return "no"
    if set(arr)!={1,2,3,4,5,6,7,}:
        return "no"
    for i in range(1,n//2+1):
        if arr[i]<arr[i-1]or(arr[i]-arr[i-1]>1):
            return "no"
    return "yes"
import sys
input =sys.stdin.read
data=input().split()
t=int(data[0])
idx=1
for _ in range(t):
    n=int(data[idx])
    arr=list(map(int,data[idx+1:idx+1+n]))
    print(is_rainbow(n,arr))
    idx+=1+n