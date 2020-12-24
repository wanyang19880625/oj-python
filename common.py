import string
import math
import collections, itertools, bisect, heapq

matrix = [[0] * 4 for i in range(3)]  ## 二维数组初始化
print(matrix)
print(chr(ord('a') + (ord('z') - ord('a') + 25) % 26))  # 字母序前一位
d = collections.defaultdict(list)  # 声明值类型为list的字典{key:list[]}
# def dfs(u,p):
#     for v in g[u]:
#         if v!=p:
#             dfs(v,u)
#             path[u].append(v)
# dfs(1,-1)
pairs = [[0, 1], [1, 2]]
fa = [i for i in range(5)]
child_sum = [1] * 5


# 并查集常用函数
def find(x):
    if x != fa[x]:
        fa[x] = find(fa[x])
    return fa[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    fa[x] = y
    # 计算并查集的交集大小
    child_sum[y] += child_sum[x]


# 求并集
for (i, j) in pairs:
    union(i, j)
for (i, j) in pairs:
    union(j, i)

print("union:", fa)

nums = [
    [1, 2, 3, 4, 5],
    [6, 7],
    [8],
    [9, 10, 11],
    [12, 13, 14, 15, 16]
]

# 二维数组的(
# 
# i,j,value)坐标值生成模板
ans, res = [], []
for (i, v) in enumerate(nums):
    for (j, n) in enumerate(v):
        res.append((i, j, n))
b = [1, 0, 0]
b.extend([0, 0])
from decimal import *

print(Decimal(1) / Decimal(100000))
a = [1, 2, 3]
t = a[:]
print(bin(3)[2:].rjust(10, '0'))


# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111x)
# ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
#        ylabel='Y-Axis', xlabel='X-Axis')
# plt.show()
# 判断n是否为素数
def isprime(n):
    if n <= 1:
        return 0
    m = int(math.sqrt(n)) + 1
    for x in range(2, m):
        if n % x == 0:
            return 0
    return 1


# 利用递归分解n并打印质因数
ans = []


def bprime(n):
    if isprime(n):
        ans.append(n)
    else:
        x = 2
        while x <= int(n / 2):
            if n % x == 0:
                ans.append(x)
                return bprime(n // x)
            x = x + 1


bprime(725760000000000000)  # 测试分解30
print(ans, len(ans))
# 求b的质因数集合
primerd = collections.defaultdict(lambda: 0)
i, b = 2, 725760000000000000
while i * i <= b:
    while b % i == 0:
        primerd[i] += 1
        b = b // i
    i += 1
if b != 1:
    primerd[b] += 1
print(primerd)

# 求数n阶乘的质因数k的个数
n, cnt, k = 8, 0, 2
tmp = n
while tmp >= k:
    cnt += tmp // k
    tmp = tmp // k
print("%d的质因数%d的个数:%d" % (n, k, cnt))

## 计算质数
primenumber = [2, 3]
n = 100000
for i in range(5, n + 1, 2):
    flag = False
    x = int(i ** 0.5)
    for j in primenumber:
        if j > x:
            flag = True
            break
        if i % j == 0:
            flag = False
            break
    if flag:
        # print(i)
        primenumber.append(i)
print(len(primenumber))

# 快速幂
mod = 998244353  # 998244353 or 10**9+7


def quickpower(v, count, p):
    tmp = 1
    while count:
        if count & 1:
            tmp = tmp * v % p
        v = v * v % p
        count = count >> 1
    return tmp


# 逆元
def inverse(a, p):
    return quickpower(a, p - 2, p)


# 取a的逆元
print("取逆元:", 1 * quickpower(4, mod - 2, mod) % mod)

# 组合
n = 11
fact = [1] * n
infact = [1] * n
for i in range(1, n):
    fact[i] = fact[i - 1] * i % mod
    infact[i] = infact[i - 1] * quickpower(i, mod - 2, mod) % mod
print("组合数:", fact[10] * infact[5] % mod * infact[10 - 5] % mod)
# 双指针区间
l, r = 0, 0
res = []
s = [3, -4, 3, -3, 44]
n = len(s)
while r < n:
    while r < n and s[l] == s[r]:
        r += 1
    res.append((s[l], r - l))
    l = r
print("双指针:", res)
print("双指针group:", [(k, len(list(g))) for k, g in itertools.groupby(s)])
def func(x):
    if x < 0:
        return '-'
    if x > 0:
        return '+'
print("双指针group by func:", [(k, list(g)) for k, g in itertools.groupby(s, key=func)])

# 等比数列,求某数在等比数列的区间编号以及区间内的位置
r, t = 30, 1
j = 0
dis = 2
while r > t:
    r = r - t
    t = t * dis
    j += 1
print("id:%d,pos:%d" % (j, r))

# 快排
# arr=[49, 38, 65, 97, 23, 22, 76, 1, 5, 8, 2, 0, -1, 22]
# def qsort(a,l,r) :
#     if l<r:
#         index=get(a,l,r)
#         qsort(a,l,index-1)
#         qsort(a,index+1,r)

# def get(a,l,r):
#     tmp=a[l]
#     while l<r:
#         while l<r and a[r]>=tmp:
#             r=r-1
#         a[l]=a[r]
#         while l<r and a[l]<=tmp:
#             l=l+1
#         a[r]=a[l]
#     a[l]=tmp
#     print (a)
#     return l
# qsort(arr,0,len(arr)-1)

test = [2, 2, 1, 2]
cnt = [0] * 3
ans1 = [0] * 3
for t in test:
    cnt[t] += 1
    ans1[t] += (cnt[t] - 1)
heap = []
heapq.heappush(heap, (1, 1))
heapq.heappush(heap, (1, 2))
heapq.heappush(heap, (1, 3))
print(heapq.heappop(heap))
a = [1, 1, 2, 2, 3, 4]
print(bisect.bisect_right(a, 10), bisect.bisect_right(a, 4), bisect.bisect_left(a, 4))
print("003000".lstrip('0'))
print("333??".count('?'))
print(list(itertools.accumulate(a)))
print("".find(""))