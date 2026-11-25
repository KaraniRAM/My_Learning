
class Solution:
    def smallestUniqueSubarray(self, nums):
        n=len(nums)
        b1=31
        b2=37
        m1=10**9+7
        m2=10**9+9
        def check(l):
            p1=pow(b1,l-1,m1)
            p2=pow(b2,l-1,m2)
            h1=0
            h2=0
            d={}
            for j in range(l):
                h1=(h1*b1+nums[j])%m1
                h2=(h2*b2+nums[j])%m2
            d[(h1,h2)]=1
            for j in range(l,n):
                old=nums[j-l]
                new=nums[j]
                h1=((h1-old*p1)*b1+new)%m1
                h2=((h2-old*p2)*b2+new)%m2
                key=(h1,h2)
                d[key]=d.get(key,0)+1
            for co in d.values():
                if co==1:
                    return True
            return False
        i=1
        j=n
        k=n
        while i<=j:
            mid=(i+j)//2
            if check(mid):
                k=mid
                j=mid-1
            else:
                i=mid+1
        return k
