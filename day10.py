class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        ans = node = l1
        while l1 or l2 or carry:
            if l1: 
                carry += l1.val
                l1 = l1.next
            if l2: 
                carry += l2.val
                l2 = l2.next
            carry, node.val = divmod(carry, 10)
            if not carry and not l1 and not l2: break
            if not node.next:
                node.next = ListNode()
            node = node.next
        return ans