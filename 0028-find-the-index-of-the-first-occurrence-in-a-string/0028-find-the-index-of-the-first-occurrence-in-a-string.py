class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        si=len(needle)
        for i in range(len(haystack)-(si-1)):
            if haystack[i:i+si]==needle:
                return i
        return -1
        