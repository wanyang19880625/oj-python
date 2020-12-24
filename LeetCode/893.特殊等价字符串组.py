#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

# @lc code=start
import collections
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        flag=[False]*len(A)
        count=0
        for i in range(0,len(A)):
            if flag[i]==False:
                dic1=collections.Counter([A[i][x] for x in range(0,len(A[i])) if x%2==0])
                dic2=collections.Counter([A[i][x] for x in range(0,len(A[i])) if x%2==1])
                for j in range(i+1,len(A)):
                    dic3=collections.Counter([A[j][x] for x in range(0,len(A[j])) if x%2==0])
                    dic4=collections.Counter([A[j][x] for x in range(0,len(A[j])) if x%2==1])
                    if dic1==dic3 and dic2==dic4:
                        flag[j]=True
                count+=1
                flag[i]=True
        return count
# @lc code=end

