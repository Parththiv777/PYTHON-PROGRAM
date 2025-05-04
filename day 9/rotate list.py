class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        p = head
        count = 1
        while p.next:
            count += 1
            p = p.next
        p.next = head    
        k = k % count
        steps = count - k
        new_tail = head
        for i in range(steps - 1):
            new_tail = new_tail.next

        head = new_tail.next
        new_tail.next = None
        return head

       
