class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        val = {

        }
        res = []
        for words in strs:
            word_signature = [0] * 26
            for letters in words:
                word_signature[ord("a") - ord(letters)] += 1
            if tuple(word_signature) not in val:
                val[tuple(word_signature)] = [words]
            else:
                val[tuple(word_signature)].append(words)
        for x in val.values():
            res.append(x)
        return res 

