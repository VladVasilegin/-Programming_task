# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        result = int(num1[::-1]) + int(num2[::-1])

        l3 = None

        for i in str(result):
            l3 = ListNode(int(i), l3)

        return l3
