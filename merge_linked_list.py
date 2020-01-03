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
		self.print_the_llist(l1)

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

# Driver module
if __name__ == '__main__':
	s = Solution()
	ls = [2,3,4,5]
	s.convert_list_to_llist(ls)
		