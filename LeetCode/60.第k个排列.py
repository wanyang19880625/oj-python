#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import itertools
        per=[''.join(x) for x in list(itertools.permutations([str(i) for i in range(1,n+1)],n))]
        # print (per)
        return per[k-1]
# @lc code=end

