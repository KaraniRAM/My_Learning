class Solution:
    def checkValidString(self, s: str) -> bool:
        l=r=0
        for ch in s:
            if ch=="(":
                l+=1
                r+=1
            elif ch==")":
                if l>0:
                    l-=1
                r-=1
            else:
                if l>0:
                    l-=1
                r+=1
            if r<0:
                return False
        return l==0