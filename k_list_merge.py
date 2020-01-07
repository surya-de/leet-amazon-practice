'''
 	Description- code to merge two sorted
 				linked list.
 	@Author: Suryadeep
'''

class ListNode:
	def __init__(self, key):
		self.val = key
		self.next = None

class Solution:
	# This module takes a list of
	# lists and converts it into
	# a list of linked lists.
	def list_to_llist(self, lst):
		ls_llist = []
		for lists in lst:
			dummy = ListNode(0)
			ptr = dummy
			for node in lists:
				ptr.next = ListNode(node)
				ptr = ptr.next
			ls_llist.append(dummy.next)
		self.sort_k_llists(ls_llist)
	# This module takes in a list of
	# linked lists and prints it to
	# properly viw the contents.
	def print_llists(self, p_list):
		for llists in p_list:
			while llists.next is not None:
				print(str(llists.val) + '->', end = '')
				llists = llists.next
			print(llists.val)
	# This module takes in a list of
	# linked lists and prints it to
	# properly viw the contents.
	def print_one_llists(self, ls):
		while ls.next is not None:
			print(str(ls.val) + '->', end = '')
			ls = ls.next
		print(ls.val)
	# This module takes a list of
	# linked lists as input and
	# sorts all the linked lists
	# into a new linked list		
	def sort_k_llists(self, l_of_llists):
		l1 = l_of_llists[0]
		for i in range(1, len(l_of_llists)):
			sorted_list = ListNode(0)
			tracker = sorted_list
			l2 = l_of_llists[i]
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

			l1 = sorted_list.next
		self.print_one_llists(l1)
# Driver code
if __name__ == '__main__':
	s = Solution()
	inp = [[1, 4, 5], [1, 3, 4],
			[2, 6]]
	s.list_to_llist(inp)