"""
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The contiguous subarray [4, -1, 2, 1] has the maximum sum (4 + (-1) + 2 + 1 = 6).
"""

input_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def calcSubarraySum(input_arr):
    max_so_far = float('-inf')
    curr = float('-inf')
    
    for val in input_arr:
        curr = max(curr+val, val)
        max_so_far = max(max_so_far, curr)
    return max_so_far

result = calcSubarraySum(input_arr=input_arr)
print(f"Max sum of subarray {input_arr} is: {result}")

"""
Explanation:
At every step, either consider total sum at that index or just the value at that index because a single element can be a subarray

Consder input => [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Start from 1st index 
maximum so far till 0th index is -2 then on index 1, total becomes -1 but what seems better is neglecting every element before that and just consider 1
Likewise, I'm maintaining 2 variables which are "curr" to maintain current sum till a specific index and max_so_far which maintains maximum subarray sum till that index

0 :: curr = -2, max_so_far = -2
1 :: curr = 1,  max_so_far = 1
2 :: curr = -2, max_so_far = 1
3 :: curr = 2,  max_so_far = 4
4 :: curr = 3,  max_so_far = 3
5 :: curr = 5,  max_so_far = 5
6 :: curr = 6,  max_so_far = 6
7 :: curr = 1,  max_so_far = 6
8 :: curr = 5,  max_so_far = 6
"""