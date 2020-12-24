#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @oj: codeforces
# @id: hitwanyang
# @email: 296866643@qq.com
# @date: 2020/12/17 17:03
# @url: https://codeforc.es/contest/1141/problem/F2
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
## py 10**6 排序+双指针 3秒可能TLE
## 按区间右端点排序,current.left>pre.right,贪心求不相交区间的最大个数
def main():
	n = int(input())
	a = list(map(int, input().split()))
	prefix = list(itertools.accumulate(a))
	d = collections.defaultdict(list)
	for i in range(n):
		for j in range(i, n):
			if i == 0:
				d[prefix[j]].append((i, j))
			else:
				v = prefix[j] - prefix[i - 1]
				d[v].append((i, j))
	ans = []
	for k in d.keys():
		v = d[k]
		cnt = []
		## 按区间右端点排序
		tmp = sorted(v,key=lambda x:(x[1],x[0]))
		if len(tmp) == 1:
			cnt.append((tmp[0][0] + 1, tmp[0][1] + 1))
		else:
			pre = tmp[0]
			## 贪心求不相交区间的最大个数
			cnt.append((pre[0] + 1, pre[1] + 1))
			for i in range(1, len(tmp)):
				cur = tmp[i]
				if cur[0] > pre[1]:
					cnt.append((cur[0] + 1, cur[1] + 1))
					pre = cur
		if len(cnt) > len(ans):
			ans = cnt
	############## TLE code ##############
	## 按区间右端点排序
	# sr = sorted(res, key=lambda x: (x[2], x[1], x[0]))
	# print(time.time() - start)
	# l, r = 0, 0
	# while r < len(sr):
	# 	pre = sr[l]
	# 	cnt = [(pre[0] + 1, pre[1] + 1)]
	# 	while r < len(sr) and sr[l][2] == sr[r][2]:
	# 		cur=sr[r]
	# 		if cur[0] > pre[1]:
	# 			cnt.append((cur[0] + 1, cur[1] + 1))
	# 			pre = cur
	# 		r += 1
	# 	l = r
	# 	if len(cnt) > len(ans):
	# 		ans = cnt
	# print (time.time()-start)

	print(len(ans))
	for a in ans:
		print(a[0], a[1])


if __name__ == "__main__":
	main()
