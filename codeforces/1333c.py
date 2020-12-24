n=int(input())
nums=input()
# 41,-41,41,-41
sum=n*(n+1)/2
a=list(map(int,nums.split()))
prefix=[a[0]]
for i in range(1,n):
    prefix.append(prefix[i-1]+a[i])
print (prefix)