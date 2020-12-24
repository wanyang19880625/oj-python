#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
import string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=[s.index(x) for x in string.ascii_lowercase if s.count(x)==1]
        return -1 if len(l)==0 else min(l)
# @lc code=end

