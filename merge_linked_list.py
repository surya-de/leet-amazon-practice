'''
 	Description- code to merge two sorted
 				linked list.
 	@Author: Suryadeep
'''

class LinkedList:
	def __init__(self, key):
		self.val = key
		self.next = None

class Solution:
	# Function to create
	# linked list from a
	# python list.
	def convert_list_to_llist(self, ls1):
		# Create a dummy list node
		# with no data value.
		dummy = LinkedList(0)
		# Initiate another list node
		# that points to the same dummy ptr.
		l1 = dummy
		# Iterate the python list
		for node in ls1:
			# Point the current node's
			# next value to the new node.
			l1.next = LinkedList(node)
			# Increment the pointer to 
			# traverse to the last node.
			l1 = l1.next
		# Update the final linked list
		# by removing the head value
		# of dummy pointer.
		l1 = dummy.next
		# Call function to print the
		# linked list.
		#self.print_the_llist(l1)
		return l1

	# Function to print the Linked
	# list.
	def print_the_llist(self, list_node):
		# Iterate the nodes through the
		# linked list.
		while list_node.next is not  None:
			# Print the linked list values.
			print(str(list_node.val) + '->', end = '')
			# Increment the pointer to 
			# traverse to the last node.			
			list_node = list_node.next
		# Print the last node.
		print(str(list_node.val))

	# Funtion to merge the
	# two sorted linked list
	def merge_llist(self, l1, l2):
		# Initialize the sorted llist
		# to retrn after merging.
		sorted_llist = LinkedList(0)
		# Pointer to traverse the
		# merged linked list.
		tracker = sorted_llist
		# Iterrate when there is
		# some value on bith the
		# linked list.
		while l1 and l2:
			# Condition check when l1
			# is more than l2.
			if l1.val > l2.val:
				# Point the tracker pointer
				# to the memory block of the
				# least value.
				tracker.next = l2
				# Move the tracker pointer to
				# read the the next value.
				#tracker = tracker.next
				# Move the List with small
				# value to next position.
				l2 = l2.next
			# Condition check when both
			# the values are equal.
			elif l1.val == l2.val:
				# Point the tracker pointer
				# to the memory block of the
				# least value.
				tracker.next = l1
				# Move the tracker pointer to
				# read the the next value.
				tracker = tracker.next
				# Move the List with small
				# value to next position.				
				l1 = l1.next
				# Point the tracker pointer
				# to the memory block of the
				# least value.
				tracker.next = l2
				# Move the tracker pointer to
				# read the the next value.				
				tracker = tracker.next
				# Move the List with small
				# value to next position.
				l2 = l2.next
			# Condition check for when l2 is
			# greater than l1
			else:
				# Point the tracker pointer
				# to the memory block of the
				# least value.
				tracker.next = l1
				# Move the tracker pointer to
				# read the the next value.
				#tracker = tracker.next
				# Move the List with small
				# value to next position.
				l1 = l1.next
			tracker = tracker.next
		# Check for any remaining
		# values in the list l1.
		while l1:
			tracker.next = l1
			tracker = tracker.next			
			l1 = l1.next
		# Check for any remaining
		# values in the list l2.
		while l2:
			tracker.next = l2
			tracker = tracker.next
			l2 = l2.next
		self.print_the_llist(sorted_llist.next)
# Driver module
if __name__ == '__main__':
	s = Solution()
	ls = [1, 2,4,5]
	ls2 = [1,3,6]
	lst1 = s.convert_list_to_llist(ls)
	lst2 = s.convert_list_to_llist(ls2)
	s.merge_llist(lst1, lst2)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # If an empty list is passed
        # return None.
        if len(lists) == 0:
            return None
        # Hold the first linked list
        # in a list element.
        l1 = lists[0]
        # Iterate through the entire
        # list starting from index 1.
        for i in range(1, len(lists)):
        	# Linked list instance to
        	# store the sorted linked
        	# list for each iteration.
            sorted_list = ListNode(0)
            # Tracker pointer to track
            # traverse through the new
            # sorted list.
            tracker = sorted_list
            # Instantiate the second
            # list to compare.
            l2 = lists[i]
            # Linked List compare and
            # merge module.
            while l1 and l2:
                if l1.val < l2.val:
                    tracker.next = l1
                    tracker = tracker.next
                    l1 = l1.next
                elif l1.val == l2.val:
                    tracker.next = l1
                    tracker = tracker.next
                    l1 = l1.next
                    tracker.next = l2
                    tracker = tracker.next
                    l2 = l2.next
                else:
                    tracker.next = l2
                    l2 = l2.next
                    tracker = tracker.next
            if l1:
                tracker.next = l1
            if l2:
                tracker.next = l2
            # Upadate the sorted list
            # into l1 instance to carry
            # on the comparison.
            l1 = sorted_list.next
        return l1