package array;

import java.util.*;
import java.util.Map.Entry;

/**
 * 
 * Problem description:
 * 
 * Given an array of integers, return indices of two numbers such that 
 * they add up to a specific target. 
 * 
 * You may assume that each input has exactly one solution. 
 * You may not use the same element twice.
 * 
 * Example:
 * 
 * Given nums = [2, 7, 11, 15], target = 9,
 * 
 * Because nums[0] + nums[1] = 2 + 7 = 9,
 * 
 * return [0, 1] or [1, 0].
 * 
 * Solution summary (using hash table): 
 * Record each entry in the array and along with its index as a key/value pair in a hash table.
 * Then, traverse the array and compute the complement of each element in the array. If the 
 * complement of that element is a key in the hash table and the value of that key is not an
 * index equal to the index of the element itself then return the appropriate indices.  
 * 
 * Time Complexity: O(n + n) = O(2n) = O(n), where n is the length of the array.
 * 
 * Space Complexity: O(n)
 *
 * pseudocode: 
 * 1) Initialize a dummy node in the solution list to zero. 
 *    The solution is then incrementally appended to this dummy node. 
 * 2) Initialize the sum variable to 0.
 * 3) Use two independent pointers to crawl through each list one node at time. 
 * 4) On each iteration of the loop, use the pointers to inspect the respective nodes and 
 *    recalculate the sum of the two summands. 
 *    The sum is composed of two digits: a sum digit and a carry digit. 
 * 5) Isolate the sum by taking the remainder after division by 10. 
 *    Initialize the next node to this sum. 
 * 6) Leave the carry in the sum variable during the next iteration of the loop 
 *    by dividing the sum variable by 10. 
 */
public class TwoSum {

	public static void main(String[] args) {
		int[] nums = {2, 7, 11, 15}; 
		int[] solution = new int[2]; 
		solution = twoSumOnePass(nums, 9);
		for(int i: solution)
			System.out.print(i + " ");
	}
	
	/**
	 * a brute force solution with time complexity O(n^2) due to the two for loops 
	 * and space complexity O(1) since we only need to allocate an array with two entries
	 * to hold the solution. 
	 * 
	 * @param nums - array of integers
	 * @param target - the goal to reach by summing two array elements 
	 * @return an array containing the indices of the two summands
	 */
	public static int[] twoSumBruteForce(int[] nums, int target) {
		//allocate the solution array
		int[] solution = new int[2]; 
		//set up two moving pointers into the array
		for(int i = 0; i < nums.length; i++) {
			for(int j = i+1; j < nums.length; j++) {
				if(nums[i] + nums[j] == target) {
					solution[0] = i;
					solution[1] = j;
				}
			}
		}
		return solution;
	}
	
	/**
	 * 
	 * @param nums - an array of ints
	 * @param target - the goal to reach by summing two array elements
	 * @return an array containing the indices of the two summands
	 */
	public static int[] twoSumFast(int[] nums, int target) {
	//initialize a Map data structure to hold pairs of Integers
	Map<Integer, Integer> map = new HashMap<>();
	//traverse the array and put each value/index pair into the map 
	//as a key/value pair
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    
    //traverse the array again and check if any of the elements in the array sums to the 
    //target when added to a key in the map
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        //if the map contains the complement as a key, and the value of that key is not i
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
    //if execution reaches here, we cannot return an integer array
    throw new IllegalArgumentException("No two sum solution");
}
	
	/**
	 * This solution uses the same idea of using a map as TwoSumFast, but uses the 
	 * "check as you go" approach such that the map only needs to be traversed once.
	 * 
	 * @param nums - an array of ints
	 * @param target - the goal to reach by summing two array elements
	 * @return an array containing the indices of the two summands
	 */
	public static int[] twoSumOnePass(int[] nums, int target) {
		//initialize an empty map
		Map<Integer, Integer> map = new HashMap<>();	
		//traverse the array and place each value/index pair in a map data structure.
		//before placing a pair in the map, check if the complement is in the map.
		for(int i = 0; i < nums.length; i++) {
			//compute the complement of the current array element
			int complement = target - nums[i];
			//check if map already contains the complement
			if(map.containsKey(complement))
				return new int[] { map.get(complement), i };
			map.put(nums[i], i);
		}
		throw new IllegalArgumentException("No two sum solution");
	}
}
