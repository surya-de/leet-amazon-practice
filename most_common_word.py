'''
	Punctuations
	` ?`, `'` , `'`,`'`, `;`, `.`
'''
from collections import Counter
class Solution:
	def max_occur(self, paragraph, banned):
		# Form word list from the
		# paragraph of strings.
		
		# Varible to store the strings
		# for each valid iteration and
		# later pushing it into list.
		s = ''
		# Insert a empty value at the
		# end of the string which acts
		# as the delimitter.
		paragraph = paragraph + ' '
		# List of all the punctuations
		# that might be available in
		# the paragraph.
		punctuations = [',', ' ', '?', "'", ';', '.', '!']
		word_list = []
		# For each character in the
		# string.
		for item in paragraph:
			# If the character is not present
			# in the punctuatuion list.
			if item not in punctuations:
				# Add the character into the
				# string.
				s += item.lower()
			else:
				# If the formed string is not in
				# the banned list and is not empty.
				if s != '' and s not in banned:
					# append the string to form
					# the word list.
					word_list.append(s)
				# Reinitiate the string.
				s = ''
		# Count the occurance of each
		# word in the list using the
		# counter container from the
		# collections class.
		cnt = Counter(elems for elems in word_list)
		# Return the most common value
		# from the counter object.
		return cnt.most_common(1)[0][0]

if __name__ == '__main__':
	s = Solution()
	para = "Bob"
	ban = []
	print(s.max_occur(para, ban))