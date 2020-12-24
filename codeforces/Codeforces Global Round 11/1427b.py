# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-10-10 22:26
# @url:https://codeforc.es/contest/1427/problem/B
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
        n,k=map(int,input().split())
        s=str(input())
        ans=0
        if k==0:
            temp=0
            for j in range(n):
                if s[j]=='W':
                    temp+=1
                else:
                    if temp!=0:
                        ans+=(1+(temp-1)*2)
                    temp=0
            if temp!=0:
                ans+=(1+(temp-1)*2)
            print (ans)
            continue
        cnt=0
        for j in range(n):
            if s[j]=='L':
                cnt+=1
        if k>=cnt:
            print (1+(n-1)*2)
            continue
        l,r=0,0
        res=[l,r]
        cnt=0
        while r<n:
            temp=cnt
            while r<n:
                if k==0:
                    if temp>cnt:
                        cnt=temp
                        res=[l,r]
                    break
                if s[r]=='L':
                    k-=1
                else:
                    temp+=1
                r+=1
            if s[l]=='L':
                temp-=1
                k=1
            l+=1
        print (res)
        # ans=
        # print (ans)
if __name__ == "__main__":
    main()