def merge_sorted(head1, head2):
  # if both lists are empty then merged list is also empty
  # if one of the lists is empty then other is the merged list
  if head1 == None:
    return head2
  elif head2 == None:
    return head1

  mergedHead = None;
  if head1.data <= head2.data:
    mergedHead = head1
    head1 = head1.next
  else:
    mergedHead = head2
    head2 = head2.next

  mergedTail = mergedHead
  
  while head1 != None and head2 != None:
    temp = None
    if head1.data <= head2.data:
      temp = head1
      head1 = head1.next
    else:
      temp = head2
      head2 = head2.next

    mergedTail.next = temp
    mergedTail = temp

  if head1 != None:
    mergedTail.next = head1
  elif head2 != None:
    mergedTail.next = head2

  return mergedHead

# Maintain a head and a tail pointer on the merged linked list. 
# Then choose the head of the merged linked list by comparing 
# the first node of both linked lists. For all subsequent nodes in both lists, 
# you choose the smaller current node and link it to the tail of the merged list, 
# and moving the current pointer of that list one step forward.

# Continue this while there are some remaining elements in both the lists. 
# If there are still some elements in only one of the lists, 
# you link this remaining list to the tail of the merged list. 
# Initially, the merged linked list is NULL.

# Compare the value of the first two nodes and make the node 
# with the smaller value the head node of the merged linked list. 
# In this example, it is 4 from head1. 
# Since it’s the first and only node in the merged list, it will also be the tail. 
# Then move head1 one step forward.