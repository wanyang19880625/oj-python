#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        flag=[False]*len(dominoes)
        num=0
        for i in range(len(dominoes)):
            count=0
            if flag[i] != True :
                for j in range(i+1,len(dominoes)):
                    f1=(dominoes[i][0]==dominoes[j][0] and dominoes[i][1]==dominoes[j][1])
                    f2=(dominoes[i][0]==dominoes[j][1] and dominoes[i][1]==dominoes[j][0])
                    if flag[j]!=True and (f1 or f2):
                        flag[i]=True
                        flag[j]=True
                        count+=1
            num+=((count+1)*count)/2
        return int(num)
        
# @lc code=end

