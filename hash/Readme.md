# 技巧
1.对于hash，主要有三种结构可以选择\
    a.使用数组，这种往往适合输入范围是一个固定值\
    b.使用dict，这种一般用于需要知道对应下标 或者需要记录个数的场景\
    c.使用set，这种一般用与只需要知道是否存在的场景\
2.对于需要有初始化值的可以使用defaultdict，这样在get的时候就不需要判断是否存在了

3.异位词---
    a.两个的hash表一样（技巧，用26为数组记录字母出现的次数，然后hash保存）,
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

    b.排序后相等
4.同构词-- 构建s，t双向映射