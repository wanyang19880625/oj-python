#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
import string
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d=dict()
        for domain in cpdomains:
            dlist=str(domain).split()
            count=int(dlist[0])
            vis=dlist[1].split('.')
            for i in range(0,len(vis)):
                temp=".".join(vis[i:len(vis)])
                if temp in d.keys():
                    d[temp]+=count
                else:
                    d[temp]=count
        return [(str(v)+" "+str(k)) for k,v in d.items()]

# @lc code=end

