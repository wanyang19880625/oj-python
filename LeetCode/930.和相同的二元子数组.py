#
# @lc app=leetcode.cn id=930 lang=python3
#
# [930] 和相同的二元子数组
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        import collections
        p=[0]
        for a in A:
            p.append(p[-1]+a)
        d=collections.Counter()
        ans=0
        for k in p:
            ans+=d[k]
            d[k+S]+=1
        return ans
        # l=0
        # t=0
        # ans=0
        # for r in range(len(A)):
        #     t=t+A[r]
        #     while l<r and t>=S:
        #         if t==S:
        #             ans+=1
        #         l+=1
        #         t=t-A[l]
        # return ans
# @lc code=end

