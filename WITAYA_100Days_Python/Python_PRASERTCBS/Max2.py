nums = [3,5,7,9,11,33]
max = nums[0]
for i in nums:
    if i > max:
        max = i


min = nums[0]
for i in nums:
    if i < min:
        min = i



print('The max value is = ',max)
print('The min value is = ',min)


