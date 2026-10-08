class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l=[]
        b=0
        for i in s:
            if i=='(':
                if b>0:
                    l.append(i)
                b+=1
            else:
                if b>1:
                    l.append(i)
                b-=1
        return "".join(l)