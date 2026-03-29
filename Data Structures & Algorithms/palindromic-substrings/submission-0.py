class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        if len(s) < 2:
            return 1

        
        for x in range(len(s)):
            res = s[x] #center
            pointer_1 = x
            pointer_2 = x
            result +=1
            while pointer_1-1 >= 0 and pointer_2+1 < len(s):
                if s[pointer_1- 1]  == s[pointer_2+1]:
                    res = s[pointer_1-1] + res + s[pointer_2 + 1]
                    pointer_1 -=1
                    pointer_2 += 1
                    result += 1
                else:
                    break
            
        for x in range(len(s) -1):
            pointer_1 = x 
            pointer_2 = x+1
            
            if s[pointer_1] != s[pointer_2]:
                continue
            result +=1
            while pointer_1-1 >= 0 and pointer_2 +1 < len(s) and s[pointer_1- 1]  == s[pointer_2+1]:
                if s[pointer_1- 1]  == s[pointer_2+1]:
                   
                    pointer_1-=1
                    pointer_2 +=1
                    result += 1
        
        return result
                
        