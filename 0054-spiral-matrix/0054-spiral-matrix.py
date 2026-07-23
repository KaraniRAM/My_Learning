class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        i = j = 0
        r = len(matrix) - 1
        c = len(matrix[0]) - 1
        g = []
        n = 0

        while n <= r and n <= c:

            while j <= c:
                g.append(matrix[i][j])
                j += 1
            j -= 1
            i += 1

            while i <= r:
                g.append(matrix[i][j])
                i += 1
            i -= 1
            j -= 1

            if n < r:
                while j >= n:
                    g.append(matrix[i][j])
                    j -= 1
                j += 1

            i -= 1

            if n < c:
                while i > n:
                    g.append(matrix[i][j])
                    i -= 1
                i += 1

            j += 1

            n += 1
            r -= 1
            c -= 1

            i = n
            j = n

        return g