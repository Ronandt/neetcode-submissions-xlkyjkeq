class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31-i))
        print(res)
        return res 
        """
        Step 1: n >> i
Say n = 1011 and i = 2. Shift everything right by 2:
1011 >> 2  =  0010
Bit that was at position 2 is now sitting at position 0 (the rightmost spot).

Step 2: & 1
1 in binary is 0001. ANDing with it zeros out everything except position 0:
0010
& 0001
------
  0000   → bit was 0

1101
& 0001
------
  0001   → bit was 1
So you're left with just a 0 or 1 — the value of that one bit.
        """