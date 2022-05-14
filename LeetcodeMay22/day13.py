class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        layer = [root]

        while layer:
            for n1, n2 in zip(layer, layer[1:]):
                n1.next = n2

            nxt = []
            for n in layer:
                if n.left:
                    nxt.append(n.left)
                if n.right:
                    nxt.append(n.right)
            layer = nxt
        return root
