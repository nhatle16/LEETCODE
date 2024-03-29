# https://leetcode.com/problems/merge-two-sorted-lists/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()  # create a dummy node as the head of merged list
    current = dummy
    
    # approach the nodes in 2 lists simultaneously
    while list1 and list2:
        if list1.val < list2.val:   # check if the node in list 1 has smaller value than that in list 2
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2    # check if the node in list 2 has smaller value than that in list 1
            list2 = list2.next
            
        current = current.next  # move to the next node in the linked list
        
    current.next = list1 if list1 else list2    # append the rest of either list 1 or list 2 to the linked list
    
    return dummy.next

if __name__ == "__main__":
    list1 = ListNode(2, ListNode(5, ListNode(7, ListNode(9))))
    list2 = ListNode(1, ListNode(1, ListNode(3, ListNode(4))))
    
    result = mergeTwoLists(list1, list2)
    
    while result:
        print(result.val, end=' -> ')
        result = result.next