class ListNode:
    '''represents one node from a linked list.'''
    def __init__ (self, x): 
        self.val = x 
        self.next = None

def make_list (python_list: list):
    '''creates a linked list from a `python_list`.'''
    root_value = python_list[0]
    root = ListNode (root_value)
    current = root

    for i in range (1, len (python_list)):
        temp = ListNode (python_list[i])
        current.next = temp
        current = current.next
    return root

def display (current):
    '''prints out all values in a linked list'''
    while (current is not None):
        print(current.val, end=' ')
        current = current.next
    print ()

if __name__ == 'main':
    # driver code
    root = make_list ([1,2,3,4,5])
    display (root)