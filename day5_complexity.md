# Reverse Array
Time complexity: O(n)
Space Complexity:O(1)

## Explanation:
the algorithm uses two pointers, one starting from the beginning and one from the end of the array.
In each iteration, the elements at these pointers are swapped and the pointers move towards the center.
Each element is visited at most once , so the total number of operations is proportional to n.
No additional data structure is used;  the reversal is done in place, so the extra space required is constant.