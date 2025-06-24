# 技巧

1.组合、分割类问题都是一个套路
```python
    def dfs(start,tmp):
        # 判断是否tmp满足
        if tmp is correct:           ------1
            ans.append(ans)
            
        # 递归回溯
        for i in range(start,len(s)):
            # 判断是否满足递归的要求
            if is_vaild():              ------2
                dfs(i,tmp+cur)           ------3
```
2.剪枝：可以把回溯的过程想成一个多叉树，对于一些明确的是不满足要求的路径可以提前结束
往往在 1 或者 2处可以进行剪枝

3.元素重复问题，
如果给的s保证了元素是不重复的，
    1.要求一个元素只能用一次 那么dfs(i,tmp+cur)  这里要进行i+1，dfs(i+1,..) ==>保证一个元素只会被用一次
    2.要求可以用多次，那么就是dfs(i,..)
如果s不保证元素是不重复的，
且要求结果不能有排列，那么有两种方式
1.先对s进行排序，然后判断s[i]==s[i-1]?==>continue
2.使用一个visited数组，在取s[i]的时候先判断s[i]是否使用过，然后 s[i]=true dfs s[i]=false