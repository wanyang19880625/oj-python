#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase=sorted(A)
        decrease=sorted(A,reverse=True)
        return A==increase or A==decrease
# @lc code=end

