class Solution:
    #打印一个新的字符串，其中每个数字字符都被替换为了number
    #扩容,从后往前
    def fn(self,s:str)->None:
        s = list(s)
        count = 0
        for v in s:
            if v.isdigit():
                count+=1
        arg = "number"
        l,nl = len(s),len(s)+count*(len(arg)-1)
        s = s+["0"]*count*(len(arg)-1)
        p1,p2 = l-1,nl-1
        while p1>=0:
            if s[p1].isdigit():
                s[p2-5:p2+1] = arg
                p2 = p2-6
                p1-=1
            else:
                s[p2] = s[p1]
                p1-=1
                p2-=1
        print(''.join(s))

if __name__ == '__main__':
    so = Solution()
    s = input("s:")
    so.fn(s)