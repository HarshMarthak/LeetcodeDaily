class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        adj_list = [[] for _ in range(n)]
        for x, y in pairs:
            adj_list[x].append(y)
            adj_list[y].append(x)
        visited = [False] * n
        d = defaultdict(list)
        p = list(range(n))
        for i in range(n):
            if visited[i]:
                continue
            stack = [i]
            visited[i] = True
            while stack:
                e = stack.pop()
                p[e] = i
                d[i].append(s[e])
                for j in adj_list[e]:
                    if not visited[j]:
                        stack.append(j)
                        visited[j] = True
            d[i].sort(reverse=True)
        l = []
        for i in range(n):
            l.append(d[p[i]].pop())
        return ''.join(l)
