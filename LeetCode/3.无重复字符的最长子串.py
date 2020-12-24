#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        d=[0]*1000
        mx=0
        for i in range(len(s)):
            t=ord(s[i])
            while d[t]>=1:
                # print (i,l)
                temp=ord(s[l])
                mx=max(i-l,mx)
                d[temp]=d[temp]-1
                l=l+1
            d[t]=d[t]+1
        return max(len(s)-l,mx)
# @lc code=end

