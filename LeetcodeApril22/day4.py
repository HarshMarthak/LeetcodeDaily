class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first=second=temp=head
        while temp.next:
                if k>1:
                    k-=1
                    first=first.next
                else:
                    second=second.next
                temp=temp.next
        first.val,second.val=second.val,first.val
        return head