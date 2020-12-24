# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-25 23:00
# @url:https://codeforces.com/contest/1328/problem/A
import sys
import collections,itertools,bisect,heapq,math,string
def input():
    return sys.stdin.readline().strip()

def main():
    t=int(input())
    nums=[list(map(int,input().split())) for x in range(t)]
    i=0
    for n in nums:
        a,b=n[0],n[1]
        if a%b!=0:
            print ((a//b+1)*b-a)
        else:
            print (0)
if __name__ == "__main__":
    main()