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

### [14.50_pow_x_n](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_3_Array_Matrix/14.50_pow_x%2Cn.py)
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

### [15_169_majority_element](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_3_Array_Matrix/15.169_majority_element.py)
###### Problem Link: https://leetcode.com/problems/majority-element/
<details><summary>Brute Force</summary>


##### TC: O(N*N)
##### SC: O(1)
##### Algorithm
1.  Check the count of occurrences of all elements of the array one by one. Start from the first element of the array and count the number of times it occurs in the array. If the count is greater than the floor of N/2 then return that element as the answer. If not, proceed with the next element in the array and repeat the process.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(N)

##### SC: O(1)
##### Algorithm
Moore’s Voting Algorithm

##### Intuition:
 The question clearly states that the nums array has a majority element. Since it has a majority element we can say definitely the count is more than N/2.

Majority element count = N/2 + x;

Minority/Other elements = N/2 – x;

Where x is the number of times it occurs after reaching the minimum value N/2.

Now, we can say that count of minority elements and majority element are equal upto certain point of time in the array. So when we traverse through the array we try to keep track of the count of elements and which element we are tracking. Since the majority element appears more than N/2 times, we can say that at some point in array traversal we find the majority element. 
1. Initialize 2 variables: 
Count –  for tracking the count of element
Element – for which element we are counting
2. Traverse through nums array.
    1. If Count is 0 then initialize the current traversing integer of array as Element 
    2. If the traversing integer of array and Element are same increase Count by 1
    3. If they are different decrease Count by 1
3. The integer present in Element is the result we are expecting 

</details>

### [16_229_majority_element_2](https://github.com/shamli1997/sde_sheet_180_problems/blob/main/sde_sheet_180_problems/Day_3_Array_Matrix/16_229_majority_element_2.py)
###### Problem Link: https://leetcode.com/problems/majority-element-ii/
<details><summary>Brute Force</summary>


##### TC: O(N*N)
##### SC: O(1)
##### Algorithm
1.  Simply count the no. of appearance for each element using nested loops and whenever you find the count of an element greater than N/3 times, that element will be your answer.
</details>

<details><summary>Most Optimal</summary>

##### TC: O(N)

##### SC: O(1)
##### Algorithm
Moore’s Voting Algorithm

##### Intuition:
1. num1 and num2 will store our currently most frequent and second most frequent element.
2. c1 and c2 will store their frequency relatively to other numbers.
3. We are sure that there will be a max of 2 elements which occurs > N/3 times because there cannot be if you do a simple math addition.
Let, ele be the element present in the array at any index. 

1. if ele == num1, so we increment c1.
2. if ele == num2, so we increment c2.
3. if c1 is 0, so we assign num1 = ele.
4. if c2 is 0, so we assign num2 = ele.
5. In all the other cases we decrease both c1 and c2.
6. In the last step, we will run a loop to check if num1 or nums2 are the majority elements or not by running a for loop check.

Intuition: Since it’s guaranteed that a number can be a majority element, hence it will always be present at the last block, hence, in turn, will be on nums1 and nums2.

</details>