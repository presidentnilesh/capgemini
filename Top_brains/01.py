
# 1

# EASY
# Subarray Removal
# Description:
# You are given an integer array nums.
# In one operation, you may remove a single contiguous subarray .
# Return the minimum length of a subarray, you must remove so that the resulting array has all distinct elements.
# If nums already has all distinct elements, return 0.
# Example 1
# Input:
# nums = [1, 2, 3, 4]
# Output:
# 0
# Explanation: Already distinct; no removal needed.
# Example 2
# Input:
# nums = [1, 2, 1, 2, 3]
# Output:
# 2
# Explanation: Remove a length-2 subarray such as [2, 1] (indices 1..2) to get [1, 2, 3], which is distinct.
# Example 3
# Input:
# nums = [2, 2, 2]
# Output:
# 2
# Explanation: Remove any two adjacent elements to leave a single 2 (distinct).