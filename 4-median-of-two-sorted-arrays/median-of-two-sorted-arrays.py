class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        # Always search in the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        low = 0
        high = m

        while low <= high:

            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Left and right values of nums1
            if partition1 == 0:
                maxLeft1 = float('-inf')
            else:
                maxLeft1 = nums1[partition1 - 1]

            if partition1 == m:
                minRight1 = float('inf')
            else:
                minRight1 = nums1[partition1]

            # Left and right values of nums2
            if partition2 == 0:
                maxLeft2 = float('-inf')
            else:
                maxLeft2 = nums2[partition2 - 1]

            if partition2 == n:
                minRight2 = float('inf')
            else:
                minRight2 = nums2[partition2]

            # Correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:

                # Odd
                if (m + n) % 2 == 1:
                    return max(maxLeft1, maxLeft2)

                # Even
                else:
                    return (
                        max(maxLeft1, maxLeft2)
                        + min(minRight1, minRight2)
                    ) / 2.0

            # Move left
            elif maxLeft1 > minRight2:
                high = partition1 - 1

            # Move right
            else:
                low = partition1 + 1