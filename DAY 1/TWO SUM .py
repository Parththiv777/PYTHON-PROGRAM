# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        uebertrag = 0
        ergebnis_start = ListNode()
        ergebnis = ergebnis_start
        while not (l1 == None and l2 == None) or uebertrag > 0:
            if l1 == None and l2 != None:
                value = (l2.val + uebertrag) % 10
                uebertrag = (l2.val + uebertrag) // 10
                l2 = l2.next
            elif l2 == None and l1 != None:
                value = (l1.val + uebertrag) % 10
                uebertrag = (l1.val + uebertrag) // 10
                l1 = l1.next
            elif l1 != None and l2 != None:
                value = (l1.val + l2.val + uebertrag) % 10
                uebertrag = (l1.val + l2.val + uebertrag) // 10
                l1 = l1.next
                l2 = l2.next
            else:
                value = uebertrag % 10
                uebertrag = uebertrag // 10
            ergebnis.val = value
            if not (l1 == None and l2 == None) or uebertrag > 0:
                next_node = ListNode()
                ergebnis.next = next_node
                ergebnis = next_node
        # ein letztes mal summen
        return ergebnis_start
