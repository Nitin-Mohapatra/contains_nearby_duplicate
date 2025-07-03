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
