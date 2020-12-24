#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
import functools
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cmp(a,b):
            acnt=bin(a).count('1')
            bcnt=bin(b).count('1')
            if acnt==bcnt:
                return -1 if (a<b) else 1
            else:
                return -1 if acnt<bcnt else 1

        return sorted(arr,key=functools.cmp_to_key(cmp))
        
        
# @lc code=end

