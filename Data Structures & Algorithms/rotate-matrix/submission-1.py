class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()
        matrix[:] = [list(row) for row in zip(*matrix)]