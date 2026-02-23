class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        a, b = headA, headB
        
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        
        return a

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


headA = ListNode(1)
headA.next = ListNode(2)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)


headB = ListNode(9)
headB.next = headA.next.next.next  # point to node with value 4

sol = Solution()
sol.getIntersectionNode(headA, headB)
