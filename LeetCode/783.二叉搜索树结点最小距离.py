#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树结点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        node=[]
        def dfs(root:TreeNode):
            if root!=None:
                dfs(root.left)
                node.append(root.val)
                dfs(root.right)
        dfs(root)
        m=2**31
        for i in range(1,len(node)):
            m=min(abs(node[i]-node[i-1]),m)
        return m
# @lc code=end

