# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict = {}
        while head != None:
            if head.val in dict.keys():
                if dict[head.val] == head.next:
                    return True
            else:
                dict[head.val] = head.next
        return False


if __name__ == "__main__":
    n = 15
    print(Solution().fizzBuzz(n))