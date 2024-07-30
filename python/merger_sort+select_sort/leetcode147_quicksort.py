class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        dummy = ListNode(0)
        cur = head

        while cur is not None:
            pre = dummy
            while pre.next is not None and pre.next.val < cur.val:
                pre = pre.next
            
            next_node = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = next_node

        return dummy.next
