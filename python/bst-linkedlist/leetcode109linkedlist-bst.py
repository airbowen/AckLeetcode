class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def getMedian(left: ListNode, right: ListNode) -> ListNode:
            # 快慢指针初始化
            fast = slow = left
            # 寻找中位节点
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def buildTree(left: ListNode, right: ListNode) -> TreeNode:
            # 基准条件
            if left == right:
                return None
            # 获取当前子链表的中位节点
            mid = getMedian(left, right)
            # 创建树节点
            root = TreeNode(mid.val)
            # 递归构建左子树
            root.left = buildTree(left, mid)
            # 递归构建右子树
            root.right = buildTree(mid.next, right)
            return root
        
        # 调用 buildTree 方法构建整个树
        return buildTree(head, None)
