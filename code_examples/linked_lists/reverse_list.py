def reverse(linked_list):
    """
    Reverse the inputted linked list

    Args:
       linked_list(obj): Linked List to be reversed
    Returns:
       obj: Reveresed Linked List
    """
    
    new_list = LinkedList()
    
    prev_node = None
    
    for value in linked_list:
        new_node = Node(value)
        new_node.next = prev_node
        prev_node = new_node
        
    new_list.head = prev_node
    
    return new_list