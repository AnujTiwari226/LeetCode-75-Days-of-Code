from typing import Optional


class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def print_list(self):
        pass


class Solution:
    def __init__(self):
        self.head = None

    def merge_two_list(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        if l1.data < l2.data:
            l1.next = self.merge_two_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_list(l1, l2.next)
            return l2

    @staticmethod
    def print_list(llist):
        h = llist
        while h:
            print(h.data, end=' ')
            h = h.next


if __name__ == '__main__':
    sol1 = Solution()
    sol1.head = ListNode(1)
    v2 = ListNode(3)
    v3 = ListNode(4)
    v4 = ListNode(6)
    sol1.head.next, v2.next, v3.next = v2, v3, v4

    sol2 = Solution()
    sol2.head = ListNode(1)
    s2 = ListNode(2)
    s3 = ListNode(3)
    s4 = ListNode(5)
    sol2.head.next, s2.next, s3.next = s2, s3, s4

    sol3 = Solution()
    sol3 = sol3.merge_two_list(sol1.head, sol2.head)
    Solution().print_list(sol3)

