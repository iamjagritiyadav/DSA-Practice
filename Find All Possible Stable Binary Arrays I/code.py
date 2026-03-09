class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]
        
        for i in range(1, min(zero, limit)+1):
            dp0[i][0] = 1
        
        for j in range(1, min(one, limit)+1):
            dp1[0][j] = 1
        
        for z in range(zero+1):
            for o in range(one+1):
                
                for k in range(1, min(limit, z)+1):
                    dp0[z][o] = (dp0[z][o] + dp1[z-k][o]) % MOD
                
                for k in range(1, min(limit, o)+1):
                    dp1[z][o] = (dp1[z][o] + dp0[z][o-k]) % MOD
        
        return (dp0[zero][one] + dp1[zero][one]) % MOD
