#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans=[]
        def dfs(root:TreeNode)->int :
            if root !=None:
                dfs(root.left)
                ans.append(root.val)
                dfs(root.right)
        dfs(root)
        return sum([x for x in ans if x>=L and x<=R])

# @lc code=end

