'''
	Punctuations
	` ?`, `'` , `'`,`'`, `;`, `.`
'''
from collections import Counter
class Solution:
	def max_occur(self, paragraph, banned):
		# Form word list from the
		# paragraph of strings.
		s = ''
		paragraph = paragraph + ' '
		punctuations = [',', ' ', '?', "'", ';', '.', '!']
		word_list = []
		for item in paragraph:
			if item not in punctuations:
				s += item.lower()
			else:
				if s != '' and s not in banned:
					word_list.append(s)
				s = ''
		cnt = Counter(elems for elems in word_list)
		
		return cnt.most_common(1)[0][0]

if __name__ == '__main__':
	s = Solution()
	para = "Bob"
	ban = []
	print(s.max_occur(para, ban))