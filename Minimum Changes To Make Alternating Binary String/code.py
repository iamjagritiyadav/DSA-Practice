class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0  # pattern starting with '0'
        count2 = 0  # pattern starting with '1'
        
        for i in range(len(s)):
            if s[i] != ('0' if i % 2 == 0 else '1'):
                count1 += 1
            if s[i] != ('1' if i % 2 == 0 else '0'):
                count2 += 1
                
        return min(count1, count2)
