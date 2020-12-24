#
# @lc app=leetcode.cn id=1362 lang=python3
#
# [1362] 最接近的因数
#

# @lc code=start
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        import math
        n1=math.ceil(math.sqrt(num+1))+1
        n2=math.ceil(math.sqrt(num+2))+1
        a,b=[],[]
        for i in range(n1,0,-1):
            if (num+1)%i==0:
                a.append(int((num+1)/i))
                a.append(i)
                break
        for i in range(n2,0,-1):
            if (num+2)%i==0:
                b.append(int((num+2)/i))
                b.append(i)
                break
        # print (a,b)
        if abs(a[0]-a[1])>abs(b[0]-b[1]):
            return b
        else:
            return a
# @lc code=end

