class Solution:
    def copyRandomList(self, head):
        memo = {}
        def deepcopy(n):
            if not n:
                return
            if n in memo:
                return memo[n]
            memo[n] = new = Node(n.val)
            new.next   = deepcopy(n.next)
            new.random = deepcopy(n.random)
            return new
        return deepcopy(head)