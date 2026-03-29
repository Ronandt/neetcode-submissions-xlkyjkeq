class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indexes = list("abcdefghijklmnopqrstuvwxyz")
        anagram_struct = {}
        final = []

        for x in strs:
            generate_list = [0] * 26
            for y in x:
                generate_list[ord(y) - ord('a')] += 1
            signature = tuple( generate_list)
            if signature not in anagram_struct:
                anagram_struct[signature] = [x]
            else:
                anagram_struct[signature].append(x)
        for x in anagram_struct.values():
            final.append(x)

        print(anagram_struct)
        return final