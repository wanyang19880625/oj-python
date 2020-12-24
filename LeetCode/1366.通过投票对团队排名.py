#
# @lc app=leetcode.cn id=1366 lang=python3
#
# [1366] 通过投票对团队排名
#

# @lc code=start
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        from functools import cmp_to_key
        rank=[[0]*26 for i in range(0,26)]
        length=len(votes[0])
        for i in range(length):
            for j in range(len(votes)):
                index=ord(votes[j][i])-ord('A')
                rank[index][i]+=1

        # print (rank)
        rlist=sorted([(chr(ord('A')+i),v) for (i,v) in enumerate(rank)],key=lambda a: (a[1],-ord(a[0])),reverse=True)
        # rlist=sorted([(chr(ord('A')+i),v) for (i,v) in enumerate(rank)],cmp_to_key(a),reverse=True)
        # rlist1=sorted(rlist,key=lambda r:(r[0],r[1]) )
        # print (rlist[:length])     
        return "".join([r[0] for r in rlist[:length]])

# @lc code=end

