from collections import deque


class Solution:
    def topological_sort(self):
        n, m = map(int, input().split())
        in_degree = [0] * (n + 1)
        result = []
        refer_map = [[] for _ in range(n + 1)]
        for _ in range(m):
            f, t = map(int, input().split())
            in_degree[t] += 1
            refer_map[f].append(t)

        q = deque()
        # 入度为0的入队
        for i in range(1, n + 1):
            if in_degree[i] == 0:
                q.append(i)
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
    so = Solution()
    so.topological_sort()
