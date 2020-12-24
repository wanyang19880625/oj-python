#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=collections.Counter(ransomNote)
        m=collections.Counter(magazine)
        for i in r:
            if i not in m or r[i]>m[i]:
                return False
        return True
# @lc code=end

