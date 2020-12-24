# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-09-08 22:28
# @url:
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
        n=int(input())
        a=list(map(int,input().split()))
        if n==1:
            print (a[0])
            continue
        a.sort()
        ans=[]
        mx=a[-1]
        f=True
        for j in range(2,math.ceil(math.sqrt(mx))+1):
            if mx%j==0:
                f=False
                break
        ans.append(a[-1])
        if f:
            ans.extend(a[:len(a)-1])
            print (" ".join([str(x) for x in ans]))
        else:
            d=collections.defaultdict(int)
            for x in a[:n-1]:
                d[x]+=1
            gg=[]
            for x in a[:n-1]:
                gg.append(math.gcd(x,mx))
            g=sorted(gg,reverse=True)
            divsor=[g[0]]
            for j in range(len(g)):
                temp=1
                for k in range(j+1,len(g)):
                    if math.gcd(divsor[-1],g[k])>temp:
                        temp=math.gcd(divsor[-1],g[k])
                        index=k
                divsor.append(temp)
            # print (divsor)
            for x in divsor:
                for j in range(1,1001):
                    if x*j in d.keys() and d[x*j]>0:
                        ans.append(x*j)
                        d[x*j]-=1
            print (" ".join([str(x) for x in ans]))
if __name__ == "__main__":
    main()