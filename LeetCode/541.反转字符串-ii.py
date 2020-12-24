#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
import math
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string=[s[x:x+k] for x in range(0,len(s),k)]
        return ''.join([string[i][::-1]+(string[i+1] if i<len(string)-1 else "") for i in range(0,len(string),2)])
# @lc code=end

