class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for x in range(n-2, -1, -1):
                newRow[x] = newRow[x + 1] + row[x]
            row = newRow
        return row[0]
            