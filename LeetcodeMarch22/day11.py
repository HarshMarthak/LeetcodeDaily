class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp=head
        size=1
        while head.next:
            head=head.next
            size+=1
        
        k=k%size
        if k==0:
            return temp
        head.next=temp
        for _ in range(1,size-k):
            temp=temp.next
        
        head=temp.next;
        temp.next=None
        
        return head
        
            