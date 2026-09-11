class Solution(object):
    def canReach(self, start, target):
        if start == target:
            return True

        if (start[0] + start[1]) % 2 == (target[0] + target[1]) % 2:
            return True

        return False