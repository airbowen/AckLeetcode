class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow,fast = head,head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 链表的中间节点其实就是slow，但是切割的时候要取中间点的下一个

        # 这里mid 不是真的中间点，而是切割后，链表的头
        mid = slow.next
        # 链表中节点切割。这里要先给第二个链表创建好头，再切割
        slow.next = None

        # 从递归的角度来看，这个过程类似于后序遍历。
        # 因为在每次递归调用中，首先会递归地处理左子链表和右子链表，然后才会处理当前链表的合并过程。
        # 所以在定义好切割 就开始递归，递归完，然后再 merge
        left = self.sortList(head)
        right = self.sortList(mid)

        # 此时都已经切割为最小
        # 归并排序的 merge 再开始
         # 合并两个排序好的子链表
        h = res = ListNode(0)  # 创建哨兵节点，便于处理
        while left and right:
            # 比较两个链表的当前节点，将较小的节点添加到合并后的链表中
            if left.val < right.val: 
                h.next = left
                left = left.next
            else: 
                h.next = right
                right = right.next
            h = h.next  # 移动到合并链表的下一个位置

        # 如果左链表还有剩余，连接到合并后的链表
        h.next = left if left else right

        # 返回合并后的链表的头节点
        return res.next