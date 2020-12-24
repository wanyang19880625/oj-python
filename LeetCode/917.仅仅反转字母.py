#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        l=list(reversed([x for x in S if str(x).isalpha()]))
        for i in range(0,len(S)):
            if S[i].isalpha() != True:
                l.insert(i,S[i])
        return "".join(l)
# @lc code=end

