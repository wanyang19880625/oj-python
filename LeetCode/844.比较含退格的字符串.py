#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s,t=[],[]
        for c in S:
            if c!='#':
                s.append(c)
            else:
                if len(s)!=0:
                    s.pop()
        for c in T:
            if c!='#':
                t.append(c)
            else:
                if len(t)!=0:
                    t.pop()
        return "".join(s)=="".join(t)
# @lc code=end

