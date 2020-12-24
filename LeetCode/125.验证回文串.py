#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a="".join([x for x in s.lower() if str(x).isalpha() or str(x).isdigit()])
        return a==a[::-1]
# @lc code=end

