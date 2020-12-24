#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        seq=[[a[x] for a in A] for x in range(0,len(A[0]))]
        l=[s for s in seq if sorted(s)==s]
        return len(A[0])-len(l)
# @lc code=end

