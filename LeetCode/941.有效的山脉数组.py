#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A)<3:
            return False
        m,n=0,0
        for i in range(1,len(A)):
            if A[i]==A[i-1]:
                return False
            if A[i]<A[i-1]:
                m=i-1
                break
        for i in range(len(A)-1,0,-1):
            if A[i]==A[i-1]:
                return False
            if A[i]>A[i-1]:
                n=i
                break
        return m==n and m!=0 and n!=0
# @lc code=end

