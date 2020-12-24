#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#

# @lc code=start
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if len(nums1)==0 or len(nums2)==0:
            return []
        h=[]
        [[heapq.heappush(h,(nums1[i]+nums2[j],i,j)) for j in range(len(nums2))]for i in range(len(nums1))]
        # print (h)
        ans=[]
        for i in range(min(k,len(h))):
            p=heapq.heappop(h)
            ans.append([nums1[p[1]],nums2[p[2]]])
        return ans
# @lc code=end

