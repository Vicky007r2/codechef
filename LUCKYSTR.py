k,n=map(int,input().split())
fav=[input().strip() for _ in range (k)]
for _ in range(n):
    s=input().strip()
    if len(s)>=47:
        print("Good")
        continue
    is_good=False
    for f in fav:
        if f in s:
            is_good=True
            break
    if is_good:
        print("Good")
    else:
        print("Bad")