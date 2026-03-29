class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(n).count("1") for n in range(n + 1)]