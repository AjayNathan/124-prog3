def max_two(nums):
	a = 0
	b = 1
	if nums[0] < nums[1]:
			a = 1
			b = 0
	for i in xrange(len(nums)):
			if i > 1:
				if nums[i] > nums[a]:
					b = a
					a = i
				elif nums[i] > nums[b]:
					b = i
	return (a, b)

def kk(nums):
	for i in xrange(len(nums)):
		a, b = max_two(nums)
		nums[a] = nums[a] - nums[b]
		nums[b] = 0

	a, _ = max_two(nums)

	return nums[a]
