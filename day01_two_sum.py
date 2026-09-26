# Day 1: Two Sum (LeetCode #1)
# Find the positions of the two numbers that add up to target.
# Approach: brute force - try every pair with nested loops.

nums = [2, 7, 11, 15]
target = 9
for i in range(0,4):
    for j in range(i+1,4):
        if nums[i]+nums[j] == target:
            print(i,j)
 