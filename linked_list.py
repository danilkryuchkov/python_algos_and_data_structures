class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#if this file was called directly, run this example
if __name__ == "__main__":
    #create a linked list
    head = LinkedListNode(1)
    head.next = LinkedListNode(2)
    head.next.next = LinkedListNode(3)
    head.next.next.next = LinkedListNode(4)
    head.next.next.next.next = LinkedListNode(5)

    #print the list
    print("Linked List:")
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

    #reverse the list
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev

    #print the list
    print("Reversed Linked List:")
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next