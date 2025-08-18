class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for v in strs:
            vs = ''.join(sorted(v))
            m[vs].append(v)
        return list(m.values())    

