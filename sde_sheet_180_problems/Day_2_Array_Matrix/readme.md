# Day 2:Array and Matrix Problems

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

### [9.287_find_duplicate_num](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_2_Array_Matrix/9.287_find_duplicate_num.py)
###### Leetcode Link: https://leetcode.com/problems/find-the-duplicate-number/
<details><summary>Brute Force</summary>


##### TC:   O(NlogN +N)  NlogN for sorting the array and O(N) for traversing through the array and checking if adjacent elements are equal or not. But this will distort the array.
##### SC: O(1)

1. Sort the array. After that, if there is any duplicate number they will be adjacent.So we simply have to check if arr[i]==arr[i+1] and if it is true,arr[i] is the duplicate number.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(N), as we are traversing through the array only once.

##### SC: O(N), as we are using extra space for frequency array.
 1. Take a frequency array of size N+1 and initialize it to 0. Now traverse through the array and if the frequency of the element is 0 increase it by 1, else if the frequency is not 0 then that element is the required answer.

</details>

<details><summary>Optimized</summary>

##### TC: O(N), Each element is visited at most twice (once in the first loop to find the duplicate and once in the second loop to restore the numbers).

##### SC: O(1), All manipulation is done in place, so no additional storage (barring one variable) is needed.
1.  Iterate over the array, evaluating each element (let's call the current element curcur).
2. Since we use negative marking, we must ensure that the current element (curcur) is positive (i.e. if curcur is negative, then use its absolute value).

3. Check if nums[cur]nums[cur] is negative.

    1. If it is, then we have already performed this operation for the same number, and hence curcur is the duplicate number. Store curcur as the duplicate and exit the loop.

    2. Otherwise, flip the sign of nums[cur]nums[cur] (i.e. make it negative). Move to the next element and repeat step 3.

4. Once we've identified the duplicate, we could just return the duplicate number. However, even though we were not able to meet the problem constraints, we can show that we are mindful of the constraints by restoring the array. This is done by changing all negative numbers to positive.

</details>

### [10.repeat_and_missing_num](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_2_Array_Matrix/10.repeat_and_missing_num.py)
###### Problem Link: https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/
<details><summary>Brute Force</summary>


##### TC: O(N) + O(N) (as we are traversing 2 times )
##### SC: O(N) As we are making new substitute array

1. Take a substitute array of size N+1 and initalize it with 0.
2. Traverse the given array and increase the value of substitute[arr[i]] by one .
3. Then again traverse the substitute array starting from index 1 to N.
4. If you find any index value greater than 1 that is repeating element A.
5. If you find any index value = 0 then that is the missing element B.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(N)

##### SC: O(1)
 1. Iterate through array
 2. mark arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
 3. if arr element is already -ve then we have our repeating number
 4. Iterate through array and check which index is having +ve ele that index + 1 is our missing number

</details>
