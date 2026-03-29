class Solution:
    def isPalindrome(self, s: str) -> bool:
        pointer_1 = 0
        pointer_2 = len(s) -1

        while pointer_1 <= pointer_2:

            while pointer_1 <= pointer_2 and not s[pointer_1].isalpha() and not s[pointer_1].isdigit():
                print("NONOO")
                pointer_1  +=1
            while pointer_1 <= pointer_2 and not s[pointer_2].isalpha() and not s[pointer_2].isdigit():
                print("HIHIHI")
                pointer_2 += -1
            if s == "0P":
        
                print(pointer_1, pointer_2)
            if pointer_1 <= pointer_2 and s[pointer_1].lower() != s[pointer_2].lower():
      
                return False
            pointer_1 +=1
            pointer_2 -=1

        return True

            