# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020-05-27 15:26
# @url:https://codeforc.es/problemset/problem/887/B
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
def main():
    n = int(input())
    a = []
    used = []
    for i in range(n):
        x = list(input().split())
        a.append(x)
        for _ in range(6):
            used.append(x[_])
    if n == 2:
        for z in range(6):
            for k in range(6):
                s = a[0][z] + a[1][k]
                if s not in used:
                    used.append(s)
                    used.append(s[::-1])
    if n > 2:
        for z in range(3):
            for g in range(6):
                for v in range(6):
                    s = a[z][g] + a[(z + 1) % 3][v]
                    if s not in used:
                        used.append(s)
                        used.append(s[::-1])
        for j in range(6):
            for k in range(6):
                for p in range(6):
                    s = a[0][j] + a[1][k] + a[2][p]
                    if s not in used:
                        used.append(s)
                        used.append(s[::-1])
    used = sorted(list(set(map(int, used))))
    if 0 in used:
        del used[used.index(0)]
    if used.count(1) > 0:
        for q in range(len(used)):
            if used[q] != q + 1:
                print(q)
                exit()
        print(used[-1])
    else:
        print(0)
if __name__ == "__main__":
    main()