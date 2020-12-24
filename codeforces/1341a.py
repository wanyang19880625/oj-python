# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-25 21:24
# @url:https://codeforces.com/contest/1341/problem/A
import sys
import collections,itertools,bisect,heapq,math,string
def input():
    return sys.stdin.readline().strip()

def main():
    t=int(input())
    nums=[list(map(int,input().split())) for x in range(t)]
    for n in nums:
        count,a,b,c,d=n[0],n[1],n[2],n[3],n[4]
        if (a-b)*count>(c+d) or (a+b)*count<(c-d):
            print ("No")
        else:
            print ("Yes")
    
            
if __name__ == "__main__":
    main()