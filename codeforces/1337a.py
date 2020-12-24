# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-25 22:00
# @url:https://codeforces.com/contest/1337/problem/A
import sys
import collections,itertools,bisect,heapq,math,string
def input():
    return sys.stdin.readline().strip()

def main():
    t=int(input())
    nums=[list(map(int,input().split())) for x in range(t)]
    i=0
    for n in nums:
        x,y,z=n[1],n[2],n[2]
        print (x,y,z)
if __name__ == "__main__":
    main()