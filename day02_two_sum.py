# Day 2: Two Sum (LeetCode #1)
# Find the positions of the two numbers that add up to target.
# Approach: dict lookup - each number x needs a partner of (target - x).
# A dict of number -> position tells us in one step if that partner exists.
# Time: O(n), down from O(n^2) for the Day 1 brute force.

nums = [2, 7, 11, 15]
target = 9

# Step A: build the dict, number -> position
# for [2, 7, 11, 15] this makes {2: 0, 7: 1, 11: 2, 15: 3}
seen = {}
for i in range(len(nums)):
    seen[nums[i]] = i

# Step B: for each number, look up its partner
for i in range(len(nums)):
    partner = target - nums[i]                   # the number nums[i] needs
    if partner in seen and seen[partner] != i:   # partner exists and isn't nums[i] itself
        print(i, seen[partner])
        break                                    # found the answer, stop looking
