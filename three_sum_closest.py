class Solution:
	def threeSumClosest(self, nums, target):
		nums.sort()
		diff = float('inf')
		for i in range(len(nums)):
			lo = i + 1
			hi = len(nums) - 1
			while lo < hi:
				add = nums[i] + nums[lo] + nums[hi]
				if abs(diff) > abs(target - add):
					diff = target - add
				if add < target:
					lo += 1
				else :
					hi -= 1
		return target - diff

if __name__ == '__main__':
	s = Solution()
	num = [-1, 2, 1, -4]
	target = 1
	s.threeSumClosest(num, target)