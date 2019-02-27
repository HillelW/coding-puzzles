package strings;
import java.util.*;

/**
 * 
 * Problem description:
 * 
 * Given a string, find the length of the longest substring without repeating characters.
 * 
 * Example 1:
 * 
 * Input: "abcabcbb"
 * Output: 3 
 * 
 * Explanation: The answer is "abc", with the length of 3. 
 * 
 * Example 2:
 * 
 * Input: "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 * 
 * Example 3:
 * 
 * Input: "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3. 
 * 
 * Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 * 
 * Solution summary: 
 *  
 * 
 * Time Complexity: 
 * 
 * Space Complexity: 
 *
 * pseudocode: 
 * 1) 
 */
public class LongestSubstringWithoutRepeatingCharacters {

	public static void main(String[] args) {
		String str = "abcabcbb";
		System.out.println(lengthOfLongestSubstringBruteForce(str));
	}

	/**
	 * brute force approach finds the longest substring without repeating characters 
	 * by checking all possible substrings and updating the solution variable whenever
	 * a longer substring is found. 
	 * 
	 * @param str - the string to check
	 * @return the length of the longest non-repeating substring
	 */
	public static int lengthOfLongestSubstringBruteForce(String str) {
        int length = str.length();
        int solution = 0;
        //check all possible substrings. If a given substring is unique, 
        //then its length is measured and compared with solution.
        for (int i = 0; i < length; i++)
            for (int j = i + 1; j <= length; j++)
                if (allUnique(str, i, j)) 
                	solution = Math.max(solution, j - i);
        return solution;
    }

	/**
	 * helper method to check if all the characters in a given string are unique using a set
	 * 
	 * @param s - a string to check
	 * @param start - beginning index
	 * @param end - final index
	 * @return true if all unique, false otherwise
	 */
    public static boolean allUnique(String s, int start, int end) {
        Set<Character> set = new HashSet<>();
        //traverse the string and continue to add characters of the 
        //string to the set. If a character is already there, return false
        for (int i = start; i < end; i++) {
            Character ch = s.charAt(i);
            if (set.contains(ch)) 
            	return false;
            set.add(ch);
        }
        return true;
    }
}

