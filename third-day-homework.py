# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#  示例：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # leetcode submit region end(Prohibit modification and deletion)
        # 利用迭代的方法，首先需要设置一个假的头节点，然后比较两个列表节点的大小
        pre = ListNode(-1)
        prev = pre
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return pre.next
    # 主要利用比较头节点的大小