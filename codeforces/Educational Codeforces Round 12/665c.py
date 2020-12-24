# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-11-13 16:43
# @url:https://codeforc.es/contest/665/problem/C
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
## 精度 print("%.10f" % ans)
## sqrt:int(math.sqrt(n))+1
## 字符串拼接不要用+操作，会超时
## 二进制转换:bin(1)[2:].rjust(32,'0')
## array copy:cur=array[::]
## oeis:example 1, 3, _, 1260, _, _, _, _, _, 12164510040883200
def main():
    s=str(input())
    t=list(s)
    l,r=0,0
    n=len(s)
    res=[]
    while r<n:
        while r<n and t[l]==t[r]:
            r+=1
        res.append((t[l],r-l))
        l=r
    last=0
    for i in range(len(res)-1):
        if res[i][1]>1:
            j=0
            while j<res[i][1]:
                if j%2==1:
                    for x in list(string.ascii_lowercase):
                        if j!=res[i][1]-1 and x!=res[i][0]:
                            t[last+j]=x
                            break
                        if j==res[i][1]-1 and x!=res[i][0] and x!=res[i+1][0]:
                            t[last+j]=x
                            break
                j+=1
        last+=res[i][1]
    for i in range(res[-1][1]):
        if i%2==1:
            for x in list(string.ascii_lowercase):
                if x!=res[-1][0]:
                    t[last+i]=x
                    break
    # print (t)
    print ("".join(t))
if __name__ == "__main__":
    main()