# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-24 17:46
# @url:https://codeforces.com/contest/1343/problem/B
import sys
import collections,itertools,bisect,heapq,math,string
def input():
    return sys.stdin.readline().strip()

def main():
    t=int(input())
    n=[int(input()) for x in range(t)]
    for i in n:
        temp=i//2
        if temp%2==1:
            print ("NO")
        else:
            print ("Yes")
            even=[x*2 for x in range(1,temp+1)]
            odd=[x*2-1 for x in range(1,temp)]
            res=even+odd+[sum(even)-sum(odd)]
            print (" ".join([str(r) for r in res]))
if __name__ == "__main__":
    main()