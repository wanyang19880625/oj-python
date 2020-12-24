# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-10-15 17:29
# @url:https://codeforc.es/contest/988/problem/C
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
def main():
    k=int(input())
    d=collections.defaultdict()
    res=[]
    f=False
    temp=[]
    for i in range(k):
        n=int(input())
        a=list(map(int,input().split()))
        temp.append(a)
    # print (temp)
    for i in range(len(temp)):
        s=sum(temp[i])
        t=temp[i]
        for j in range(len(t)):
            if s-t[j] in d.keys() and d[s-t[j]] != i+1:
                f=True
                res.append(d[s-t[j]])
                res.append(i+1)
                res.append(s-t[j])
                break
            d[s-t[j]]=i+1
        # print (d)
        if f:
            break
    if not f:
        print ("NO")
    else:
        print ("YES")
        first,second=temp[res[0]-1],temp[res[1]-1]
        for j in range(len(first)):
            if sum(first)-first[j]==res[2]:
                print (res[0],j+1)
                break
        for j in range(len(second)):
            if sum(second)-second[j]==res[2]:
                print (res[1],j+1)
                break
if __name__ == "__main__":
    main()