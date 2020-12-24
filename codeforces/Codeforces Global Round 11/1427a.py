# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-10-10 22:26
# @url:https://codeforc.es/contest/1427/problem/A
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
        s=sum(a)
        if s==0:
            print ("NO")
            continue
        pos,neg,zero=[],[],[]
        for x in a:
            if x>0:
                pos.append(x)
            if x==0:
                zero.append(x)
            if x<0:
                neg.append(x)
        res=[]
        f=False
        if len(pos)==0:
            res.extend(neg)
            res.extend(zero)
            print (" ".join([str(x) for x in res]))
            continue
        if len(neg)==0:
            res.extend(pos)
            res.extend(zero)
            print (" ".join([str(x) for x in res]))
            continue
        sp=sum(pos)
        sn=sum(neg)
        # print (pos,neg)
        pj=-1
        for j in range(len(pos)):
            if sp-pos[j]!=abs(sn):
                f=True
                pj=j
                break
        if pj!=-1:
            print ("YES")
            res.extend(neg)
            res.extend(zero)
            res.extend([pos[x] for x in range(len(pos)) if x!=pj])
            res.append(pos[pj])
            print (" ".join([str(x) for x in res]))
            continue
        pn=-1
        for j in range(len(neg)):
            if abs(sn-neg[j])!=sp:
                f=True
                pn=j
                break
        if pn!=-1:
            print ("YES")
            res.extend(pos)
            res.extend(zero)
            res.extend([neg[x] for x in range(len(neg)) if x!=pn])
            res.append(neg[pn])
            print (" ".join([str(x) for x in res]))
        
if __name__ == "__main__":
    main()