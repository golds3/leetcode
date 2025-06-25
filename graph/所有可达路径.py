from typing import List
class Solution:
    """
    邻接矩阵 n个元素--n*n， 建议(n+1)*(n+1)
    """
    def dfs_1(self,n,edge):
        def build_array():
            _arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
            for _ in range(m):
                # 无向图
                i,j = map(int, input().split())
                arr[i][j],arr[j][i] = 1,1
            return _arr
        arr = build_array()
        result = []
        def dfs(cur,path):
            if path[-1] == n:
                result.append(path)
                return
            for i in range(n + 1):
                if arr[cur][i]:
                    dfs(i,path+[i])

        dfs(1,[])
        if not result:
            print(-1)
        for v in result:
            print(' '.join(map(str, v)))
    """
    邻接表
    """
    def dfs_2(self,n,edge):
        def build_array():
            _arr = [[] for _ in range(n + 1)]
            for _ in range(m):
                f,t = map(int, input().split())
                _arr[f].append(t)
            return _arr
        arr = build_array()
        result = []
        def dfs(cur,path):
            if path[-1] == n:
                result.append(path)
                return
            for v in arr[cur]:
                dfs(v,path+[v])
        dfs(1,[1])
        if not result:
            print(-1)
        for v in result:
            print(' '.join(map(str, v)))


    def bfs(self,n):
        # todo
        pass



if __name__ == '__main__':
    s = Solution()
    while True:
        try:
            n_m = input().split()
            n, m = int(n_m[0]), int(n_m[1])
            s.dfs_2(n,m)
        except EOFError:
            break




# int dir[4][2] = {0, 1, 1, 0, -1, 0, 0, -1}; // 表示四个方向
# // grid 是地图，也就是一个二维数组
# // visited标记访问过的节点，不要重复访问
# // x,y 表示开始搜索节点的下标
# void bfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int x, int y) {
#     queue<pair<int, int>> que; // 定义队列
#     que.push({x, y}); // 起始节点加入队列
#     visited[x][y] = true; // 只要加入队列，立刻标记为访问过的节点
#     while(!que.empty()) { // 开始遍历队列里的元素
#         pair<int ,int> cur = que.front(); que.pop(); // 从队列取元素
#         int curx = cur.first;
#         int cury = cur.second; // 当前节点坐标
#         for (int i = 0; i < 4; i++) { // 开始想当前节点的四个方向左右上下去遍历
#             int nextx = curx + dir[i][0];
#             int nexty = cury + dir[i][1]; // 获取周边四个方向的坐标
#             if (nextx < 0 || nextx >= grid.size() || nexty < 0 || nexty >= grid[0].size()) continue;  // 坐标越界了，直接跳过
#             if (!visited[nextx][nexty]) { // 如果节点没被访问过
#                 que.push({nextx, nexty});  // 队列添加该节点为下一轮要遍历的节点
#                 visited[nextx][nexty] = true; // 只要加入队列立刻标记，避免重复访问
#             }
#         }
#     }
#
# }