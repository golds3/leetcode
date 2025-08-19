# blank 返回长度为 n 的由空格组成的字符串
from typing import List



class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格；
        # 当前行不是最后一行，且只有一个单词：该单词左对齐，在行末填充空格；
        # 当前行不是最后一行，有多个单词，多余的空格分配在左边
        ans = []
        index, n = 0, len(words)
        while True:
            start = index  # 记录每行的第一个单词的索引
            sumLen = 0  # 当前行的单词长度
            while index < n and sumLen + len(words[index]) + index - start <= maxWidth:
                # index-start -- 每个单词间至少一个空格
                sumLen += len(words[index])
                index += 1
            if index == n:
                # 已经遍历完所有单词，说明最后一行,后面补齐空格
                s = ' '.join(words[start:])
                ans.append(s + (maxWidth - len(s)) * ' ')
                break
            wordsNums = index - start
            spaceNums = maxWidth - sumLen
            if wordsNums == 1:
                # 当前行只能放一个单词，补齐空格
                ans.append(words[start] + spaceNums * ' ')
                continue
            # 当前行有多个单词
            avgSpace = spaceNums // (wordsNums - 1)  # 单词间均匀分布的空格数
            extraSpace = spaceNums % (wordsNums - 1)  # 多余的空格
            # 多余的空格放在左边，假设多余2个，那么前两组单词间隔多放1个单词
            leftS = ((avgSpace + 1) * ' ').join(words[start:start + 1 + extraSpace])
            # 右边的均匀空格
            rightS = (avgSpace * ' ').join(words[start + extraSpace + 1:index])
            ans.append(leftS + (avgSpace * ' ') + rightS)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))