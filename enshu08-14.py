from random import choice
import string

nums = string.digits
print(nums)
print(choice(nums) + choice(nums) + choice(nums) + choice(nums))
