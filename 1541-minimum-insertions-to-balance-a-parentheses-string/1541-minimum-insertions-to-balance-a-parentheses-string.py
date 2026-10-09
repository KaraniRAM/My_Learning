class Solution:
    def minInsertions(self, s: str) -> int:
        stack=[]
        i=0
        ans=0
        while i<len(s):
            ch=s[i]
            if ch=="(":
                stack.append(ch)
                i+=1
            else:
                if i+1<len(s) and s[i]==s[i+1]:
                    if stack:
                        stack.pop()
                    else:
                        ans+=1
                    i=i+2
                else:
                    if stack:
                        ans+=1
                        stack.pop()
                    else:
                        ans+=2
                    i+=1
        if stack:
            ans+=len(stack)*2
        return ans

        
            