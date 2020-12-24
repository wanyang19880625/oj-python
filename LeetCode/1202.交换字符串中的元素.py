#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#

# @lc code=start
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: [int]) -> str:
        import collections
        fa=[i for i in range(len(s))]
        # 并查集函数
        def find(x):
            if x!=fa[x]:
                fa[x]=find(fa[x])
            return fa[x]
        def union(x,y):
            x = find(x)
            y = find(y)
            if x == y:  
                return
            fa[x] = y
        # 求并集
        for (i,j) in pairs:
            union(i,j)
        for (i,j) in pairs:
            union(j,i)
        d=collections.defaultdict(list)
        for (i,j) in enumerate(fa):
            d[j].append(i)
        ans=['']*len(s)
        for p in d.values():
            temp=sorted([s[i] for i in p])
            # print (p,temp)
            for (k,v) in zip(p,temp):
                ans[k]=v
        return "".join(ans)
        
# @lc code=end

