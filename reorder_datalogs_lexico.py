'''
	Important concepts are-
	1. Key in sorted.
	2. lambda interpretation
		of the sorted function
	3. How a function can be
		used in the key part
		of sorted function.
'''
class Solution(object):
	def reorderLogFiles(self, logs):
        # Utility function to return
        # the criteria based on which
        # the sorting needs to be done.
		def f(log):
            # Tuple of id and the remaining
            # part of the string.
			identifier, remain = log.split(' ', 1)
            # Check if the remaining part is
            # digit or alphabet.			
			if remain[0].isalpha():
                # If it is alphabet then return a tuple
                # with starting 0 and then the ramaining
                # string followed by the identifier as
                # that is the order in which the string
                # will be sorted.
				return (0, remain, identifier)
            # If digit then retun 1 as for this case
            # no sorting is required.		
			else:
				return (1,)
		# Return the sorted list.
        # This is similar to lambda notion
        # the key value takes the criteria
        # based on which the list will be
        # sorted. The critera is provoded
        # by the return of the function.
		return sorted(logs, key = f)
if __name__ == '__main__':
	s = Solution()
	ls = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
	print(s.reorderLogFiles(ls))