# 🔄 Contains Nearby Duplicate (Python)

This repository contains a Python solution to the **Contains Nearby Duplicate** problem—commonly seen in coding interviews and platforms like LeetCode.

---

## 📘 Problem Statement

Given an integer array `nums` and an integer `k`, return **True** if there are two distinct indices `i` and `j` in the array such that:nums[i] == nums[j] and abs(i - j) <= k. Otherwise, return **False**.

---

## 🧠 Approach

- Use a **hash map (`seen`)** to store each number along with its latest index.
- Traverse the array using `enumerate()`:
  - If the number has been seen before:
    - Check if the distance between current and previous index is less than or equal to `k`.
    - If yes, return `True`.
    - Otherwise, update the index of the number.
- If no such pair is found after traversal, return `False`.

---

## 🧾 Python Code

```python
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for idx, ele in enumerate(nums):
            if ele in seen:
                if idx - seen[ele] <= k:
                    return True
                else:
                    seen[ele] = idx
            else:
                seen[ele] = idx
        return False

# Example usage
s1 = Solution()
print(s1.containsNearbyDuplicate([1, 2, 3, 1], 3))  # Output: True


