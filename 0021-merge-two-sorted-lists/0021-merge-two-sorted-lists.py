# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # filter out all possibilities where at least one of the list is empty
        if not list1 and not list2:
            return ListNode(0).next
        if not list1:
            return list2
        if not list2:
            return list1

        result = []
        while list1 and list2:
            if list1.val <= list2.val:
                result.append(list1)
                list1 = list1.next
            else:
                result.append(list2)
                list2 = list2.next

        while list1:
            result.append(list1)
            list1 = list1.next

        while list2:
            result.append(list2)
            list2 = list2.next

        for i in range(len(result)-1):
            result[i].next = result[i+1]
        result[-1].next = None
        return result[0]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def next_list(self, next_list):
        self.next = next_list


a = ListNode(2)
a1 = ListNode(3)
a.next = a1
b = ListNode(1)
b1 = ListNode(1)
b.next = b1

print(Solution().mergeTwoLists(a, b))