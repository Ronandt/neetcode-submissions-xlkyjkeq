class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        longest = ""
        
        for x in range(len(s)):
            res = s[x] #center
            pointer_1 = x
            pointer_2 = x
            while pointer_1-1 >= 0 and pointer_2+1 < len(s):
                if s[pointer_1- 1]  == s[pointer_2+1]:
                    res = s[pointer_1-1] + res + s[pointer_2 + 1]
                    pointer_1 -=1
                    pointer_2 += 1
                else:
                    break
            if len(res) > len(longest):
                longest = res
        for x in range(len(s) -1):
            pointer_1 = x 
            pointer_2 = x+1
            if s[pointer_1] != s[pointer_2]:
                continue
            res = s[pointer_1] + s[pointer_2]
            while pointer_1-1 >= 0 and pointer_2 +1 < len(s) and s[pointer_1- 1]  == s[pointer_2+1]:
                
                res = s[pointer_1 -1] + res + s[pointer_2 + 1]
                pointer_1-=1
                pointer_2 +=1
              
            if len(res) > len(longest):
                longest = res 
        return longest
                
        