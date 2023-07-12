def add(nums):
    if len(nums) == 1:
        return nums[0]

    return nums[0] + add(nums[1:])

temp = [123,332,3,32]

print(add(temp))