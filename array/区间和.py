n = int(input())
arr = [0] * (n + 1)
# 构造前缀和数组
for i in range(1, n + 1):
    arr[i] = int(input()) + arr[i - 1]
try:
    while True:
        s = [int(v) for v in input().split()]
        start,end = s[0],s[1]
        print(arr[end+1]-arr[start])
except EOFError:
    pass
