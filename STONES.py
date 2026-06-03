import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        jewels = set(input_data[idx])
        stones = input_data[idx + 1]
        idx += 2
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        print(count)
if __name__ == '__main__':
    solve()