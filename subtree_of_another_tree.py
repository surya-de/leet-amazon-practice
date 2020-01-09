'''
	# Find a subtree.
	# Perform pre- ordet traversa of both the trees.
	# Find substring of the traversal string.
	-------------------------------------------
	# Add lnull and rnull srting values at the
	# end of each leaf node.
	# This will help aid in the string matching.
	tree s-					   | 	tree t-		
			3				   |	 		4
	4				5		   |	 	1		2
1		2		4			   |
	0						   |
	preorder- 3->4->1->2->0->5 | preorder- 4->1->2

	without lnull and r-null padding, the tree_t will become
	a substring of tree_s
	--------------------------------------------
	# Add '#' before each node value to identify
	# 2-digit numbers.
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left  = None
		self.right = None

class Solution:
	def isSubtree(self, s, t):
		# Module to perform preorder
        # travesal.
		def pre_order_traverse(node, id):
			# If not a node
			if not node:
                # Check if it is a left
                # node.				
				if id:
					return 'l-None'
                # Check if it is a right
                # node				
				if not id:
					return 'r-None'
            # Return the traversed string
            # with padded characters.
			return '#' + str(node.val) + ' ' + pre_order_traverse(node.left, True) + ' ' + pre_order_traverse(node.right, False)
		# Traversed string for tree s.
		preorder_s = pre_order_traverse(s, None)
		# Traversed string for tree t.
		preorder_t = pre_order_traverse(t, None)
		# If not a substring return False
		if preorder_s.find(preorder_t) == -1:
			return False
		return True
if __name__ == '__main__':
	s = Solution()
	root = TreeNode(3)
	root.left = TreeNode(4)
	root.right = TreeNode(5)
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(2)
	root1 = TreeNode(4)
	root1.left = TreeNode(1)
	root1.right = TreeNode(2)
	print(s.isSubtree(root, root1))