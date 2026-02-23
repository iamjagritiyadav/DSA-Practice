class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        
        # Quick rejection
        if n - k + 1 < (1 << k):
            return False
        
        seen = set()
        current = 0
        
        for i in range(n):
            # Left shift and add current bit
            current = ((current << 1) & ((1 << k) - 1)) | int(s[i])
            
            if i >= k - 1:
                seen.add(current)
        
        return len(seen) == (1 << k)
