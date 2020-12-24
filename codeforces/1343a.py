# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-24 21:49
# @url:https://codeforces.com/contest/1343/problem/A
import sys
import collections,itertools,bisect,heapq,math,string
def input():
    return sys.stdin.readline().strip()

def main():
    t=int(input())
    n=[int(input()) for x in range(t)]
    for i in n:
        for k in range(2,50):
            power=2**k-1
            if i%power==0:
                print (i//power)
                break

if __name__ == "__main__":
    main()