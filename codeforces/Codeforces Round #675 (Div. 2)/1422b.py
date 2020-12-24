# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-10-08 23:34
# @url:https://codeforc.es/contest/1422/problem/B
import sys,os
from io import BytesIO, IOBase
import collections,itertools,bisect,heapq,math,string
from decimal import *
# region fastio

BUFSIZE = 8192

BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# ------------------------------
## 注意嵌套括号!!!!!!
## 先有思路,再写代码,别着急!!!
## 先有朴素解法,不要有思维定式,试着换思路解决
def main():
    t=int(input())
    for i in range(t):
        n,m=map(int,input().split())
        matrix=[]
        for j in range(n):
            temp=list(map(int,input().split()))
            matrix.append(temp)
        # print (matrix)
        ans=0
        for j in range(n//2):
            for k in range(m//2):
                a=matrix[j][k]
                b=matrix[j][m-1-k]
                c=matrix[n-1-j][m-1-k]
                d=matrix[n-1-j][k]
                res=[a,b,c,d]
                sr=sorted(res)
                # median number
                median=(sr[2]+sr[1])//2
                ans+=abs(sr[2]-sr[1])+abs(sr[0]-median)+abs(sr[3]-median)
                # for s in range(1,5):
                #     x=abs(res[s%4]-res[(s-1)%4])
                #     y=res[s%4]+res[(s-1)%4]
                #     op=min(op,x+abs(res[(s+1)%4]-y//2)+abs(res[(s+2)%4]-y//2))
                # ans+=op
        if n%2==1:
            for j in range(m//2):
                a=matrix[n//2][j]
                b=matrix[n//2][m-1-j]
                ans+=abs(a-b)
        if m%2==1:
            for j in range(n//2):
                a=matrix[j][m//2]
                b=matrix[n-1-j][m//2]
                ans+=abs(a-b)
        print (ans)
        
if __name__ == "__main__":
    main()