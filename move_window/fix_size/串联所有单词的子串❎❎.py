from collections import Counter, defaultdict
from typing import List


class Solution:
    """
        给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

     s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

    例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
    返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
    """

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 定长滑动窗口
        ans = []
        word_len = len(words[0])
        windows_len = word_len * len(words)
        # 注意这里的target_cnt ，如果不在words的单词，它的value=0
        target_cnt = Counter(words)
        # 对s进行分组，只需要进行word_len次滑动滑口即可
        # 假设word_len =3 ，那么s 可以按照如下进行划分
        # 1. s[0:3],s[3:6],s[6:9] ....
        # 2. s[1:4],s[4:7],s[7:10] ...
        # 3. s[2:5],s[5:8],s[8:11]
        # 那么对于i>wold_len的情况其实已经包含在上面了 比如i=3 s[3:6] in case 1 ; s[4:7] in case 2; s[5:8] in case 3
        for start in range(word_len):
            cnt = defaultdict(int)
            overload = 0  # 记录是否超过target_cnt
            for right in range(start + word_len, len(s) + 1, word_len):
                cur_word = s[right - word_len : right]
                if cnt[cur_word] == target_cnt[cur_word]:
                    # 不在words的单词和在words的单词
                    overload += 1
                cnt[cur_word] += 1
                left = right - windows_len
                if left < 0:
                    # 窗口长度不够
                    continue
                if overload == 0:
                    ans.append(left)
                # 左窗口出
                out_word = s[left : left + word_len]
                cnt[out_word] -= 1
                if cnt[out_word] == target_cnt[out_word]:
                    overload -= 1
        return ans


if __name__ == "__main__":
    print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best"]))
