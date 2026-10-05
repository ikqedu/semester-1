# Worksheet 1.2: Task 2 Solution
from util import read_file

nums = read_file()

if len(nums) == 0:
    exit("Error: no numbers provided")

min_num = min(nums)
max_num = max(nums)
mean_num = sum(nums) / len(nums)

if len(nums) % 2 == 0:
    median_num = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
else:
    median_num = sorted(nums)[len(nums) // 2]

print(f"Minimum = {min_num}\nMaximum = {max_num}\nMean={mean_num}\nMedian={median_num}")

