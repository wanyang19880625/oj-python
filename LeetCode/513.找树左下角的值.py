#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        import collections
        q=collections.deque()
        q.append(root)
        value=root.val
        while q:
            top=q.popleft()
            if top.right!=None:
                q.append(top.right)
            if top.left!=None:
                q.append(top.left)
            value=top.val
        return value
            
# @lc code=end

