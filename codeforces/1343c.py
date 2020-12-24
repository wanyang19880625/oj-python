# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-25 11:21
# @url:https://codeforces.com/contest/1343/problem/C
import sys
import collections,itertools,bisect,heapq,math,string
def input():
    return sys.stdin.readline().strip()

def main():
    t=int(input())
    num=[]
    for i in range(t):
        n=int(input())
        temp=list(map(int,input().split()))
        num.append(temp)
    index=0
    while index<t:
        mx=0
        a=num[index]
        temp=[a[0]]
        # print (a)
        for i in range(1,len(a)):
            if (a[i-1]>0 and a[i]<0) or (a[i-1]<0 and a[i]>0):
                temp.append(a[i])
            else:
                if temp[-1]<a[i]:
                    temp[-1]=a[i]
        print (sum(temp))
        index+=1
 

if __name__ == "__main__":
    main()