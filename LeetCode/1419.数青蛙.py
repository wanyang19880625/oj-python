#
# @lc app=leetcode.cn id=1419 lang=python3
#
# [1419] 数青蛙
#

# @lc code=start
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        letter=['c','r','o','a','k']
        if len(croakOfFrogs)%5!=0:
            return -1
        import collections
        d=collections.defaultdict()
        for i in range(len(letter)):
            d[letter[i]]=i
        cnt=[0]*5
        for s in croakOfFrogs:
            index=d[s]
            if index==0:
                cnt[index]+=1
            else:
                cnt[index-1]-=1
                cnt[index]+=1
        print (cnt)
        if cnt[0]!=cnt[3]:
            return -1
        else:
            return cnt[4]

# @lc code=end

