#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p=paragraph.lower().replace(","," ").replace("."," ")
        plist=p.replace(";"," ").replace("!"," ").replace("?"," ").replace("'"," ").split(" ")
        d=sorted(collections.Counter(plist).items(),key=lambda p:p[1],reverse=True)
        # print (d)
        for x in d:
            if x[0] not in banned and x[0]!='':
                return x[0]
        return ""
# @lc code=end

