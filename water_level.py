class Solution:
    def maxArea(self, height):
    	start = 0
    	end = len(height) - 1
    	weight = -999
    	while start < end:
    		weight = max(weight, min(height[start], height[end]) * (end - start))
    		if height[start] < height[end]:
    			start += 1
    		else:
    			end -= 1
    	return weight

if __name__ == '__main__':
	s = Solution()
	h = [1,8,6,2,5,4,8,3,7]
	s.maxArea(h)