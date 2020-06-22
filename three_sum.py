class Solution:
	def threeSum(self, nums):
		op = []
		nums.sort()
		for i in range(len(nums)):
			if nums[i] > 0:
				break
			if i == 0 or nums[i - 1] != nums[i]:
				lo = i + 1
				hi = len(nums) - 1
				while lo < hi:
					sum = nums[i] + nums[lo] + nums[hi]
					print(sum)
					if sum > 0 or (hi < len(nums) - 1 and nums[hi + 1] == nums[hi]):
						hi -= 1
					elif sum < 0 or (lo > i + 1 and nums[lo - 1] == nums[lo]):
						lo += 1
					else:
						op.append((nums[i], nums[lo], nums[hi]))
						hi -= 1
						lo += 1
		print(op)

if __name__ == '__main__':
	s = Solution()
	nums = [-2,0,0,2,2]
	s.threeSum(nums)