#
# @lc app=leetcode.cn id=1477 lang=python3
#
# [1477] 找两个和为目标值且不重叠的子数组
#

# @lc code=start
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        import collections,bisect
        prefix=[0]
        for i in range(len(arr)):
            prefix.append(prefix[-1]+arr[i])
        pos=[]
        d=collections.defaultdict()
        for i,p in enumerate(prefix):
            d[p]=i
        s=sorted(set(d.keys()))
        for k in s:
            if (k+target) in s:
                pos.append((d[k],d[k+target]-1,d[k+target]-d[k]))
        # print (pos)
        if len(pos)<2:
            return -1
        if len(pos)==2:
            if pos[1][0]>pos[0][1]:
                return pos[1][2]+pos[0][2]
            else:
                return -1
        l=[x[1] for x in pos] 
        r=[x[0] for x in pos[::-1]]
        m,n=[],[]
        x=len(arr)+1
        for i in range(len(pos)-1):
            x=min(x,pos[i][2])
            m.append(x)
        x=len(arr)+1
        for i in range(len(pos)-1,0,-1):
            x=min(x,pos[i][2])
            n.append(x)
        # print (m)
        # print (n)
        # print (l)
        # print (r)
        dp=[]
        for i in range(len(r)-1):
            if r[i]<=l[0]:
                break
            low,high=0,len(l)-2
            while low<high:
                mid=(low+high+1)//2
                if l[mid]<r[i]:
                    low=mid
                else :
                    high=mid-1
            # print (low,i)
            dp.append(m[low]+n[i])
        # print (dp)
        if len(dp)==0:
            return -1
        else:
            return min(dp)
# @lc code=end

