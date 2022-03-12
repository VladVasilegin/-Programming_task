# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==0 or head.next==None:
            return head
        start=ListNode(0,head)
        new=head
        end=head
        check=head
        count=1
        while check.next!=None:
            count+=1
            check=check.next
        k=k%count
        if k==0:
            return start.next
        for i in range(k):
            end=end.next
        while end.next!=None:
            end=end.next
            new=new.next
        start.next=new.next
        new.next=None
        end.next=head
        return start.next