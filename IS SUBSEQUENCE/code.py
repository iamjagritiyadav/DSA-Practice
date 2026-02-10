class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S, T = len(s), len(t)

        if S == 0:
            return True
        if S > T:
            return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                j += 1
                if j == S:
                    return True

        return False
