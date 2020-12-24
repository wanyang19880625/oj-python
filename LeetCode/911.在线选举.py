#
# @lc app=leetcode.cn id=911 lang=python3
#
# [911] 在线选举
#

# @lc code=start
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        c0,c1=0,0
        vote=[]
        for i in range(len(persons)):
            if persons[i]==0:
                c0+=1
            else:
                c1+=1
            if c0==c1:
                vote.append(persons[i])
            elif c0>c1:
                vote.append(0)
            elif c1>c0:
                vote.append(1)
        self.vote=vote
        self.times=times
    def q(self, t: int) -> int:
        l,r=0,len(self.times)-1
        while l<r:
            mid=(l+r+1)//2
            if self.times[mid]<=t:
                l=mid
            else:
                r=mid-1
        return self.vote[l]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

