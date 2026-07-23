class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
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
            while j >= n and n<r:
                    g.append(matrix[i][j])
                    j -= 1
            j += 1
            i -= 1
            while i > n and n<c:
                    g.append(matrix[i][j])
                    i -= 1
            i += 1
            j += 1
            n += 1
            r -= 1
            c -= 1

           
        return g