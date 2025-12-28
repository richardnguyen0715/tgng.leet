def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    setlist = set()
    while head:
        if head not in setlist:
            setlist.add(head)
            head = head.next
        else:
            return True
    return False