from collections import deque
import bisect

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        start = s.count('0')
        
        if start == 0:
            return 0
        
        # Prepare sorted lists of unvisited states
        even = list(range(0, n + 1, 2))
        odd = list(range(1, n + 1, 2))
        
        # Remove start from its parity list
        if start % 2 == 0:
            even.remove(start)
        else:
            odd.remove(start)
        
        dist = [-1] * (n + 1)
        dist[start] = 0
        
        q = deque([start])
        
        while q:
            m = q.popleft()
            
            c1 = max(k - (n - m), 0)
            c2 = min(m, k)
            
            lnode = m + k - 2 * c2
            rnode = m + k - 2 * c1
            
            target = even if lnode % 2 == 0 else odd
            
            idx = bisect.bisect_left(target, lnode)
            
            while idx < len(target) and target[idx] <= rnode:
                nxt = target[idx]
                dist[nxt] = dist[m] + 1
                q.append(nxt)
                target.pop(idx)  # remove visited
                # do NOT increment idx (since we popped)
        
        return dist[0]
