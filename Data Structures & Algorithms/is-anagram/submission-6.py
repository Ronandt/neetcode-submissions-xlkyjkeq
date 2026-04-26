class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_map = [0] * 26
        for x in s:
            freq_map[ord("a") - ord(x)] += 1
        for x in t:
            freq_map[ord("a") - ord(x)] -=1
        for x in freq_map:
            if x != 0:
                return False
        return True





