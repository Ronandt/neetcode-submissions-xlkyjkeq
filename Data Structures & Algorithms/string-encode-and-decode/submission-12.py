class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for x in strs:
            encoded += str(len(x)) + "#"  + x
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        current = ""
        number = ""
        parsing_num = True
        res = []
        for x in s:
            print("how many interations")
          
            if x == "#" and parsing_num:
                if number == "0":
                    res.append("")
                    number = ""
                    continue
                parsing_num = False
                number = int(number)
                continue
            if parsing_num:
                number += x
                continue
            current += x  
            number -= 1    
            if number in [0]:
                parsing_num = True
                number = ""
                res.append(current)
                current = ""   
        print(number)
      
        return res         
    
