#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序查找树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans=[]
        def dfs(r):
            if r is not None:
                dfs(r.left)
                ans.append(r.val)
                dfs(r.right)
        dfs(root)
        dummy=TreeNode(0)
        head=dummy
        index=0
        while index<len(ans) :
            head.right=TreeNode(ans[index])
            head=head.right
            index+=1
        return dummy.right
# @lc code=end

