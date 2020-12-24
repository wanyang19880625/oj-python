#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1238] 循环码排列
#

# @lc code=start
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        ans=[start]
        for i in range(n):
            s=ans[-1]
            print (s)
            ans.append(s^(1<<i))
        return ans
# @lc code=end

