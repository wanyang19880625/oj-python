#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic=dict()
        for i in range(0,len(s)):
            if s[i] in dic.keys():
                if dic.get(s[i]) != t[i]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
                dic.setdefault(s[i],t[i])
        return True
# @lc code=end

