class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode()
        dummy2 = ListNode()
        ptr1 = dummy1
        ptr2 = dummy2
        tmp = head
        while tmp:
            if tmp.val < x:
                ptr1.next = tmp
                ptr1 = ptr1.next
            else:
                ptr2.next = tmp
                ptr2 = ptr2.next
            tmp = tmp.next
        ptr2.next = None
        ptr1.next = dummy2.next
        return dummy1.next
