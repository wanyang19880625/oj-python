#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020/12/16 10:10
# @url: https://codeforc.es/contest/1462/problem/E2
import sys, os
from io import BytesIO, IOBase
import collections, itertools, bisect, heapq, math, string
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
## sqrt:Decimal(x).sqrt()避免精度误差
## 无穷大表示:float('inf')
def main():
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        ans = 0
        mod = 10 ** 9 + 7

        def quickpower(v, count, p):
            tmp = 1
            while count:
                if count & 1:
                    tmp = tmp * v % p
                v = v * v % p
                count = count >> 1
            return tmp

        # 组合
        fact = [1] * (n + 1)
        infact = [1] * (n + 1)
        for j in range(1, n + 1):
            fact[j] = fact[j - 1] * j % mod
            infact[j] = infact[j - 1] * quickpower(j, mod - 2, mod) % mod

        pos = -1
        for j in range(n - m + 1):
            if j != 0 and a[j] == a[j - 1]:
                if pos != -1 and pos - j >= m:
                    cnt = pos - j - 1
                    ans += fact[cnt] * infact[m - 1] % mod * infact[cnt - (m - 1)] % mod
                continue
            pos = bisect.bisect_right(a, a[j] + k)
            if pos - j >= m and a[pos - 1] <= a[j] + k:
                cnt = pos - j - 1
                ans += fact[cnt] * infact[m - 1] % mod * infact[cnt - (m - 1)] % mod
        print(ans % mod)


if __name__ == "__main__":
    main()
