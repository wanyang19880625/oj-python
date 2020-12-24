# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-11-17 11:11
# @url:https://codeforc.es/contest/915/problem/C
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
    a=int(input())
    b=int(input())
    if len(str(a))<len(str(b)):
        ans=sorted(list(str(a)),reverse=True)
        print ("".join(ans))
        return
    cnt=[0]*10
    for i in range(len(str(a))):
        cnt[int(str(a)[i])]+=1
    ans=[]
    f=True
    for x in [int(i) for i in str(b)]:
        mx=-1
        for j in range(10):
            if cnt[j]>0:
                if j<=x:
                    mx=max(mx,j)
        if mx==-1:
            f=False
            break
        if mx<x:
            cnt[mx]-=1
            ans.append(mx)
            break
        if mx==x:
            cnt[x]-=1
            ans.append(x)
    # print (cnt)
    res=[]
    for i in range(10):
        if cnt[i]>0:
            res+=[i]*cnt[i]
    sr=sorted(res,reverse=True)
    # print (ans,f,sr)
    if f:
        tmp=ans+sr
        print ("".join([str(x) for x in tmp]))
    else:
        n=len(str(a))
        for i in range(len(ans)-1,-1,-1):
            j=0
            while j<len(sr):
                if sr[j]<ans[i]:
                    ans[i],sr[j]=sr[j],ans[i]
                    tmp=ans[:i+1]+sorted(ans[i+1:]+sr,reverse=True)
                    print ("".join([str(x) for x in tmp]))
                    return
                j+=1
            sr.append(ans[i])
            ans.pop(-1)
        print (a)
if __name__ == "__main__":
    main()