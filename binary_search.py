import bisect
a=[0,1,1,1,1,1,1,2,3,4,7]
l,r=0,len(a)-1
while l<r:
    mid=(l+r)//2
    if a[mid]>=1:
        r=mid
    else :
        l=mid+1
print (l)

l,r=0,len(a)-1
while l<r:
    mid=(l+r+1)//2
    if a[mid]<=1:
        l=mid
    else :
        r=mid-1
print (l)
