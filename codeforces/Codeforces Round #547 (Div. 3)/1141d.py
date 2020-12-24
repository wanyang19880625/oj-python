#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020/12/14 19:06
# @url: https://codeforc.es/contest/1141/problem/D
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
def main():
	n = int(input())
	s = str(input())
	t = str(input())
	ds = collections.defaultdict(list)
	dt = collections.defaultdict(list)
	d = collections.defaultdict(list)
	for i in range(n):
		ds[s[i]].append(i)
		dt[t[i]].append(i)
	# print(ds, dt)
	ans = []
	q = '?'
	k1, k2 = 0, 0
	for x in list(string.ascii_lowercase):
		i, j = 0, 0
		while i < len(ds[x]) or j < len(dt[x]):
			if i < len(ds[x]) and j < len(dt[x]):
				ans.append((ds[x][i] + 1, dt[x][j] + 1))
				i += 1
				j += 1
			if i >= len(ds[x]) and j < len(dt[x]):
				if q in ds.keys() and k1 < len(ds[q]):
					ans.append((ds[q][k1] + 1, dt[x][j] + 1))
					k1 += 1
				else:
					break
				j += 1
			if i < len(ds[x]) and j >= len(dt[x]):
				if q in dt.keys() and k2 < len(dt[q]):
					ans.append((ds[x][i] + 1, dt[q][k2] + 1))
					k2 += 1
				else:
					break
				i += 1
	while k1 < len(ds[q]) and k2 < len(dt[q]):
		ans.append((ds[q][k1] + 1, dt[q][k2] + 1))
		k1 += 1
		k2 += 1
	print(len(ans))
	for a in ans:
		print(a[0], a[1])


if __name__ == "__main__":
	main()
