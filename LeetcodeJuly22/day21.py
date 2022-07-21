class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        p = dummy = ListNode(None)
        dummy.next = head
        for i in range(left-1):
            p = p.next
        tail = p.next

        for i in range(right-left):
            tmp = p.next
            p.next = tail.next
            tail.next = tail.next.next
            p.next.next = tmp
        return dummy.next
