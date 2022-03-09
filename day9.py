class Solution:
    def deleteDuplicates(self, head):
        p1 = temp = ListNode(0)
        temp.next = head
        while p1:
            p2 = p1.next
            while p2 and p2.next and p2.val == p2.next.val:
                p2 = p2.next
            if p1.next is p2:
                p1 = p1.next
            else:
                p1.next = p2.next
        return temp.next