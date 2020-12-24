# @oj: atcoder
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-10-24 20:18
# @url:https://atcoder.jp/contests/arc106/tasks/arc106_b
import sys,os
from io import BytesIO, IOBase
import collections,itertools,bisect,heapq,math,string
from decimal import *
# region fastio
sys.setrecursionlimit(1000000)
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
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if n==1:
        print ("Yes")
        return
    g=[[] for i in range(n+1)]
    # for auto(u) v!=p dfs(u,v)
    for i in range(m):
        x,y=map(int,input().split())
        g[x].append(y)
        g[y].append(x)
    # print (g)
    path=[]
    v=[False]*(n+1)
    # dfs to get path,start from which vertex has only one edge
    # tle
    def dfs(p,temp):
        for i in g[p]:
            if not v[i]:
                v[i]=True
                temp.append(i)
                dfs(i,temp)
    for i in range(len(g)):
        if len(g[i])==1 and not v[g[i][0]]:
            v[i]=True
            temp=[i]
            dfs(i,temp)
            path.append(temp)
    # print (path)
    for p in path:
        temp=[(b[i-1]-a[i-1]) for i in p]
        # print (temp)
        if sum(temp)!=0:
            print ("No")
            return
    print ("Yes")
    return
    # path=[[] for i in range(n+1)]
    # def dfs(u,p):
    #     for v in g[u]:
    #         if v!=p:
    #             dfs(v,u)
    #             path[u].append(v)
    # dfs(1,-1)
    # print (path)
    
if __name__ == "__main__":
    main()