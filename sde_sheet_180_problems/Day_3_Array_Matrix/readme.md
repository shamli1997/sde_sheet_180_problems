# Day 3:Array and Matrix Problems

### [13.74_search_2d_matrix](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_3_Array_Matrix/13.74_search_2d_matrix.py)
###### Problem Link: https://leetcode.com/problems/search-a-2d-matrix/
<details><summary>Brute Force</summary>


##### TC: O(M * N)
##### SC: O(1)
##### Algorithm
1.  We can traverse through every element that is present in the matrix and return true if we found any element in the matrix is equal to the target integer.
2. If the traversal is finished we can directly return false as we did not find any element in the matrix to be equal to the target integer.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(log(M*N))

##### SC: O(1)
##### Algorithm
 1. As it is clearly mentioned that the given matrix will be row-wise and column-wise sorted, we can see that the elements in the matrix will be in a monotonically increasing order. So we can apply binary search to search the matrix. Consider the 2D matrix as a 1D matrix having indices from 0 to (m*n)-1 and apply binary search.
 2. Initially have a low index as the first index of the considered 1D matrix(i.e: 0) and high index as the last index of the considered 1D matrix(i.e: (m*n)-1).
 3. Now apply binary search. Run a while loop with the condition low<=high. Get the middle index as (low+high)/2.We can get the element at middle index using matrix[middle/m][middle%m].
 4. If the element present at the middle index is greater than the target, then it is obvious that the target element will not exist beyond the middle index. So shrink the search space by updating the high index to middle-1. 
 5. If the middle index element is lesser than the target, shrink the search space by updating the low index to middle+1.
 6. If the middle index element is equal to the target integer, return true.
 7. Once the loop terminates we can directly return false as we did not find the target element.

</details>'

### [14.50_pow_x_n](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_3_Array_Matrix/14.50_pow_x_n.py)
###### Problem Link: https://leetcode.com/problems/powx-n/
<details><summary>Brute Force</summary>


##### TC: O(N)
##### SC: O(1)
##### Algorithm
1.  Looping from 1 to n and keeping a ans variable. Now every time your loop runs, multiply x with ans. At last, we will return the ans.
2. Now if n is negative we must check if n is negative, if it is negative divide 1 by the and.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(log N)

##### SC: O(1)
##### Algorithm
1. Initialize ans as 1.0  and store a duplicate copy of n i.e nn using to avoid overflow
2. Check if nn is a negative number, in that case, make it a positive number.
3. Keep on iterating until nn is greater than zero, now if nn is an odd power then multiply x with ans ans reduce nn by 1. Else multiply x with itself and divide nn by two.
4. Now after the entire binary exponentiation is complete and nn becomes zero, check if n is a negative value we know the answer will be 1 by ans.

</details>