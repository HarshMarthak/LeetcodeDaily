class Solution:
    def networkDelayTime(self,times,n,k):
        dist = [float('inf')] * n
        dist[k-1] = 0
        for _ in range(n-1):
            stop = 1
            for u,v,d in times:
                if dist[u-1]+d < dist[v-1]:
                    dist[v-1] = dist[u-1]+d
                    stop = 0
            if stop: break
        return max(dist) if max(dist)<float('inf') else -1
