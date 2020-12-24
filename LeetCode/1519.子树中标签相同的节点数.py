#
# @lc app=leetcode.cn id=1519 lang=python3
#
# [1519] 子树中标签相同的节点数
#

# @lc code=start
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        import collections
        import sys
        sys.setrecursionlimit(10**7)
        d=collections.defaultdict(list)
        # 保存每个字母作为根节点时，子树的数量之和(数量包含节点本身)
        cnt=[0]*26
        ans=[0]*len(labels)
        def dfs(u,parent):
            index=ord(labels[u])-ord('a')
            # 保存到达该节点之前的值和
            pre=cnt[index]
            # 该节点数量增加1
            cnt[index]=cnt[index]+1
            # 遍历无向图的邻边
            for x in d[u]:
                # 由于是无向图，注意排除父节点
                if x!=parent:
                    dfs(x,u)
            ans[u]=cnt[index]-pre
        # 建立无向图
        for e in edges:
            d[e[0]].append(e[1])
            d[e[1]].append(e[0])
        # 根节点为0
        dfs(0,-1)
        return ans
# @lc code=end

