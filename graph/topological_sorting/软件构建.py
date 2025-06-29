from collections import deque


class Solution:
    def fn(self):
        n, m = map(int, input().split())
        in_degree = [0] * n
        result = []
        refer_map = [[] for _ in range(n)]
        for _ in range(m):
            f, t = map(int, input().split())
            in_degree[t] += 1
            refer_map[f].append(t)

        q = deque()
        # 入度为0的入队
        for k,v in enumerate(in_degree):
            if v == 0:
                q.append(k)
        while q:
            cur = q.popleft()
            # 加入结果集
            result.append(cur)
            # 删除节点的引用
            for v in refer_map[cur]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        if len(result) != n:
            # 有环
            print("-1")
        else:
            print(*result)




if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            s.fn()
        except Exception:
            break