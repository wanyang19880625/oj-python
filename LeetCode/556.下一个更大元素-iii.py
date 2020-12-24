#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        import itertools
        nlist=[int(''.join(x)) for x in list(itertools.permutations(str(n)))]
        print (nlist)
        index=nlist.index(n)
        if index==len(nlist):
            return -1
        else:
            return 
        
# @lc code=end

