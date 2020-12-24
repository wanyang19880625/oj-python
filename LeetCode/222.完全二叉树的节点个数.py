#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans=0
    def countNodes(self, root: TreeNode) -> int:
        def dfs(r):
            if r!=None:
                dfs(r.left)
                dfs(r.right)
                self.ans+=1
        dfs(root)
        return self.ans
# @lc code=end

