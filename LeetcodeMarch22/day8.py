class Solution:
    def hasCycle(self, head):
        hare = tortoise = head
        while hare and hare.next:
            
            tortoise = tortoise.next
            hare = hare.next.next
            
            if hare==tortoise:
                return True
        
        return False