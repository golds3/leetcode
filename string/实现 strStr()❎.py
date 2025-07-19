class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def get_next():
            """
            :return: 下标减-1的next数组
            """
            j = -1
            next = [0] * len(needle)
            next[0] = j
            for i in range(1, len(needle)):
                while j >= 0 and needle[i] != needle[j + 1]:
                    j = next[j]
                if needle[i] == needle[j + 1]:
                    j += 1
                next[i] = j
            return next

        next = get_next()
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j + 1]:
                j = next[j]
            if haystack[i] == needle[j + 1]:
                j += 1

            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1



    def strStr_2(self, haystack: str, needle: str) -> int:
        def get_next():
            """
            :return: 下标不减-1的next数组
            """
            j = 0
            next = [0]*len(needle)
            next[0] = j
            for i in range(1,len(needle)):
                while j>0 and needle[i]!=needle[j]:
                    j = next[j-1]
                if needle[i]==needle[j]:
                    j+=1
                next[i] = j
            return next
        next = get_next()
        j=0
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j = next[j-1]
            if haystack[i]==needle[j]:
                j+=1

            if j == len(needle):
                return i-len(needle)+1
        return -1



if __name__ == '__main__':
    s1, s2 = input().split()
    print(Solution().strStr(s1, s2))
