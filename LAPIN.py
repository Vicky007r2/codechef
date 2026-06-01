t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    if n % 2 == 0:
        first = s[:n//2]
        second = s[n//2:]
    else:
        first = s[:n//2]
        second = s[n//2 + 1:]
    if sorted(first) == sorted(second):
        print("YES")
    else:
        print("NO")