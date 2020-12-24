# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-04-28 09:45
# @url:https://codeforces.com/contest/1342/problem/C
import sys,os
from io import BytesIO, IOBase
import collections,itertools,bisect,heapq,math,string
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
# 1
# 172 45 10
# 7125700536461767 248534443125967684
# 356317972221852647 924249555622881273
# 49099163247633898 908533179410550830
# 405062621292215163 994454881121523458
# 498097382302378415 627453996173078973
# 268235195089903929 365145167050547336
# 214279450026044219 859057317032866567
# 394354551303356845 594628688331536337
# 929208184826745910 976725242745771529
# 755274501645946484 876743881016550392
# 1
# 55 82 10
# 673 911
# 46 277
# 771 940
# 562 758
# 92 331
# 294 825
# 469 532
# 573 901
# 442 866
# 643 875
def main():
    t=int(input())
    i=0
    while i<t:
        abq=list(map(int,input().split()))
        a,b,q=abq[0],abq[1],abq[2]
        lcm=a*b//math.gcd(a,b)
        lr=[]
        for j in range(q):
            temp=list(map(int,input().split()))
            lr.append((temp[0],temp[1]))
        
        i+=1
    print (lcm,lr)
    ans,index=[],0
    while b<t:

        index+=1
    #         if r<=min(a,b):
    #             ans.append(0)
    #         else:
    #             mod=[]
    #             for k in range(min(lcm,r-l+1)):
    #                 mod1=((l+k)%a)%b
    #                 mod2=((l+k)%b)%a
    #                 mod.append((mod1,mod2))
    #             cnt=(r-l+1)//lcm
    #             m=(r-l+1)%lcm
    #             ans.append(cnt*len([x for x in mod if x[0]!=x[1]])+len([x for x in mod[0:m] if x[0]!=x[1]]))
    print (" ".join([str(a) for a in ans]))
if __name__ == "__main__":
    main()