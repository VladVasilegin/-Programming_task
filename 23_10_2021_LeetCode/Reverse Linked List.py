# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        resultHead = None
        while head != None:
            resultHead = ListNode(head.val,resultHead)
            head = head.next
        return resultHead

if __name__ == "__main__":
    n = 15
    print(Solution().fizzBuzz(n))