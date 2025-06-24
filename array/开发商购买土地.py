n_m = input().split()
n,m = int(n_m[0]),int(n_m[1])
arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    temp = [int(v) for v in input().split()]
    for j in range(1,m+1):
        arr[i][j] = temp[j-1] + arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
print(arr)

ans = float('inf')
# 按行切分
for i in range(1,n+1):
    sa = arr[i][m]
    sb = arr[n][m] - sa
    ans = min(ans,abs(abs(sa)-abs(sb)))

# 按列切分
for i in range(1,m+1):
    sa = arr[n][i]
    sb = arr[n][m] - sa
    ans = min(ans, abs(abs(sa) - abs(sb)))
print(ans)