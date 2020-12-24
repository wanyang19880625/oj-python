#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        path=[]
        def dfs(r,p,s,v):
            if r!=None:
                p.append(r.val)
                v+=r.val
                if r.left==None and r.right==None and v==s:
                    # 注意python深拷贝用p[:],直接temp=p是浅拷贝,p变化会导致temp变化
                    temp=p[:]
                    path.append(temp)
                    # print (temp,p,path)
                dfs(r.left,p,s,v)
                dfs(r.right,p,s,v)
                p.pop(-1)
        dfs(root,[],sum,0)
        # print (path)
        return path
# @lc code=end

