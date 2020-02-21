#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) = Linear Time, there is only one operation performed for each iteration while a < n^3


b) O(n log n), the for loop is complexity O(n), and the nested inner loop is complexity O(log n).
   j is multiplied by 2, getting it half way closer to n.


c) O(n), the recursive call is called once per n

## Exercise II

This problem can be solved similarly to using binary search. Split the floor in half, throw, check to see if it breaks. If it breaks check the middle half of the lower end if it doesn't check the upper half.

The runtime complexity is O(logn) because we're constantly cutting it in half.
