### [7.48_rotate_image](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_2_Array_Matrix/7.48_rotate_image.py)
###### Leetcode Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
<details><summary>Brute Force</summary>


##### TC: O (N ^ 2)  to linearly iterate and put it into some other matrix.
##### SC: O (N ^ 2) to copy it into some other matrix.

1. Take another dummy matrix of n*n, and then take the first row of the matrix and put it in the last column of the dummy matrix.
2. take the second row of the matrix, and put it in the second last column of the matrix and so.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(N ^ 2)
##### SC: O(1)
 1. By observation, we see that the first column of the original matrix is the reverse of the first row of the rotated matrix, so that’s why we transpose the matrix and then reverse each row, and since we are making changes in the matrix itself space complexity gets reduced to O(1).
 2. Transpose of the matrix. (transposing means changing columns to rows and rows to columns)
 3. Reverse each row of the matrix.

</details>