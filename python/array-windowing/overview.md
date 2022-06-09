# Windowing Techniques

Windowing techniques are often useful for optimization problems that involve a *linear* data structure such as a list. 

When used to solve optimization problems, windowing can be understood as a dynamic programming technique. 

In particular, dynamic programming techniques can be applied whenever we are confronted with an optimization problem which exhibits *optimal sub-structure* and whose brute force solution involves *overlapping sub-problems*.

*Optimal sub-structure* means the solution to the optimization problem we want to solve can be constructed if we have access to the solutions to smaller optimization problems. This is another way of saying that optimzation problems which exhibit optimal sub-structure are susceptible to be solved using recursive techniques.

Instead of using a recursive solution to solve such problems, we can instead use windowing techniques which will not blow the stack, and will often have better performance than a recursive approach.

*Overlapping sub-problems* means the brute force solution involves much repeated unecessary work.

For exapmle, the longest or shortest sequence of a sub-list that satisfies a given condition exhibits overlapping sub-problems.

Most of the time, the sliding window technique leads to O(N) and O(1) time and space complexities, respectively.

There are two main windowing techniques:

1. Static windowing
2. Dynamic windowing

## Static Windowing

A *static window* is a sub-list of *fixed length* that runs over some list.

for example, given the list [a, b, c, d], a static window of length 2 will see the follwowing sub-lists in order:

1. [a, b]
2. [b, c]
3. [c, d]

Staic windowing techniques often do *not* lead to performant solutions. 

For example, consider the Minimum Window Substring problem. In this problem, we are given a string, and a set of characters to look for in that string. The goal is to find the smallest substring of the string that contains the given characters. If we use a static windowing technique to solve this problem by looking at a window of fixed size on each traversal of the list, then we end up with a solution that is O(n^2).

The reason for this slowness is that by constraining the algorithm to look at fixed length windows on each pass, the algorithm ends up re-examining a lot of parts of the string that don’t need to be re-examined.

In other words, *a lot of good work is being thrown out, leading a lot of useless work being done to compensate*.

## Dynamic Windowing

A *dynamic window* is a sub-list of *variable length* that runs over some list.

Depening upon the nature of the problem being solved, there are various flavors of dynamic windowing that can be used (there are only so many ways that two pointers can be used to traverse a list in linear time).

Once we decide that we want to use a dynamic windowing approach and which pieces of information to record, we need to answer the following two questions:

1. What condition should control the growth of the window? 
2. What condition should control the contraction of the window?

Some common flavors of dynamic windowing are:

1. Expand/Contract - one pointer expands the window until a valid window is found. a second pointer then contracts the window until it becomes invalid. Ex: Leetcode 76. 

2. Expand/Collapse - one pointer expands the window until the window becomes invalid and the second pointer jumps to the position of the first pointer, thereby collapsing the window. 

3. Fast/Trailing - one pointer leads the way while the second pointer lags behind by one or two indexes.

4. Contracting - the pointers start on opposite ends of the list and slowly move towards each other based on some condition. the stopping condition is that the pointers have passed each other. Ex: Binary search.
