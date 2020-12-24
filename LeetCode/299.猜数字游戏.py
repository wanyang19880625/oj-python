#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

import collections
# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        unmatchs=""
        unmatchg=""
        cnts,cntg=0,0
        for i in range(0,len(secret)):
            if secret[i]==guess[i]:
                cnts=cnts+1
            else:
                unmatchs+=secret[i]
                unmatchg+=guess[i]
        dics=collections.Counter(unmatchs)
        dicg=collections.Counter(unmatchg)
        print (dics)
        for i in dics:
            if i in dicg:
                cntg+=min(dics[i],dicg[i])
        return str(cnts)+"A"+str(cntg)+"B"
                
# @lc code=end

