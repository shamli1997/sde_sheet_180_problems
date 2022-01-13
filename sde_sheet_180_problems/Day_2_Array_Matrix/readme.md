### [7.48_rotate_image](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_2_Array_Matrix/7.48_rotate_image.py)
###### Leetcode Link: https://leetcode.com/problems/rotate-image/
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

### [8.56_merge_intervals](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_2_Array_Matrix/8.56_merge_intervals.py)
###### Leetcode Link: https://leetcode.com/problems/merge-intervals/
<details><summary>Brute Force</summary>


##### TC:   O(NlogN)+O(N*N). O(NlogN) for sorting the array, and O(N*N) because we are checking to the right for each index which is a nested loop.
##### SC: O(N), as we are using a separate data structure.

1. First check whether the array is sorted or not.If not sort the array.
2. Now linearly iterate over the array and then check for all of its next intervals whether they are overlapping with the interval at the current index. 
3. Take a new data structure and insert the overlapped interval. 
4. If while iterating if the interval lies in the interval present in the data structure simply continue and move to the next interval.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(NlogN) + O(N). O(NlogN) for sorting and O(N) for traversing through the array.
##### SC: O(N) to return the answer of the merged intervals.
 1. Linearly iterate over the array if the data structure is empty insert the interval in the data structure.2. If the last element in the data structure overlaps with the current interval we merge the intervals by updating the last element in the data structure.
 3. and if the current interval does not overlap with the last element in the data structure simply insert it into the data structure.

</details>