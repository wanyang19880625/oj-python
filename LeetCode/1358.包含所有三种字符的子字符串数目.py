#
# @lc app=leetcode.cn id=1358 lang=python3
#
# [1358] 包含所有三种字符的子字符串数目
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abcset=set()
        count,index=0,0
        while index<len(s):
            if len(abcset)<3:
                abcset.add(s[index])
            else:
                
            index+=1
# @lc code=end

