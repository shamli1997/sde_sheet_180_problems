# Day 1:Array and Matrix Problems

### 1.73. Set Matrix Zeroes (https://leetcode.com/problems/set-matrix-zeroes/)
<details><summary>Brute Force</summary>

##### TC: (N x M) x (N + M) (Traversel of the Array) x (Traversal of the row and col)
##### SC: O(1)
###### What are the ranges of the values at the matrix? (Assume all the values are on the positive side of 0)
###### 1. Traverse the matrix. Whenever gets 0 traverse for its entire row and column and place a value that can not be part of matrix (put -1 as we are told that all matrix values will be positive)
###### 2. Wherever there is -1 fill that up with 0
</details>

<details><summary>Optimized</summary>

##### TC: 2 x O(N x M) (Linear Traversel of the Array Twice)
##### SC: O(1)
###### 1.Take 2 dummy arrays (size of rows,size of col)
###### 2. Linearly traverse through array and set 0 in the 2 arrays.
###### 3. For every given index check index in col,row array and if any of it 0 make 0 in the matrix.
</details>
<details><summary>Most Optimal</summary>

##### TC: O(N x M + N x M) (Linear Traversel of the Array Twice)
##### SC: O(N) + O(M) (Two dummy row and col arrays)
###### 1. Take the dummy row,col in the matrix itself mat[0,0]
###### 2. col = True
###### 3. Iterate through matrix if you encounter 0 mark 0 in thae dummy row and col in the matrix.
##### 4. If the encountered 0 lies in the dummy col then make col = False
###### 5. Once done linear traversal traverse from back and check if any of the element in the dummy row or col is 0 make the current element 0.
###### 6. Once done linear traversal traverse from back and check if any of the element in the dummy row or col is 0 make the current element 0.
###### 7. Why did we traverse from back? It would have updated our dummy array as well if we would have started from front.
</details>

### 2.118. Pascal's Triangle(https://leetcode.com/problems/pascals-triangle/)
<details><summary>Most Optimal</summary>

##### TC: O(N) 
##### SC: O(1)
###### 1. Craete a List[List[int]] with all 1s. [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1]].
###### 2. Iterate over this List and add pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

</details>