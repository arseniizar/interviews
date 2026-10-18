# Technical Interview Preparation (`interviews`)

Curated solutions, patterns, and implementations for technical coding interviews across Data Structures & Algorithms, Systems, and Backend Engineering.

<p align="center">
  <a href="https://leetcode.com/u/arseniizar/">
    <img src="https://img.shields.io/badge/LeetCode-arseniizar-FFA116?style=for-the-badge&logo=leetcode&logoColor=white" alt="LeetCode" />
  </a>
  <a href="https://neetcode.io/practice">
    <img src="https://img.shields.io/badge/NeetCode%2075-57%2F75%20-22c55e?style=for-the-badge&logo=target" alt="NeetCode 75" />
  </a>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </a>
</p>

<p align="center">
  <a href="https://leetcode.com/u/arseniizar/">
    <img src="https://leetcard.jacoblin.cool/arseniizar?theme=dark&font=baloo" alt="Arsenii Zarudniuk LeetCode Stats" />
  </a>
</p>


---

## Problems by Topic

### 1. [Arrays & Hashing](./01_arrays_and_hashing/)
* [Two Sum](./01_arrays_and_hashing/001_two_sum.py) (Easy) - One-pass hash map
* [Palindrome Number](./01_arrays_and_hashing/009_palindrome_number.py) (Easy) - Base-10 digit reversal
* [Roman to Integer](./01_arrays_and_hashing/013_roman_to_integer.py) (Easy) - Subtractive notation
* [Group Anagrams](./01_arrays_and_hashing/049_group_anagrams.py) (Medium) - Hash map with sorted string key
* [Longest Consecutive Sequence](./01_arrays_and_hashing/128_longest_consecutive_sequence.py) (Medium) - Hash set sequence start check
* [Contains Duplicate](./01_arrays_and_hashing/217_contains_duplicate.py) (Easy) - Set length comparison
* [Product of Array Except Self](./01_arrays_and_hashing/238_product_of_array_except_self.py) (Medium) - Prefix and postfix products
* [Valid Anagram](./01_arrays_and_hashing/242_valid_anagram.py) (Easy) - Character count with Counter
* [Top K Frequent Elements](./01_arrays_and_hashing/347_top_k_frequent_elements.py) (Medium) - Frequency count with Counter
* [Contiguous Array](./01_arrays_and_hashing/525_contiguous_array.py) (Medium) - Prefix sum with 0 mapped to -1
* [Maximum Subarray](./01_arrays_and_hashing/053_maximum_subarray.py) (Medium) - Kadane's algorithm for maximum contiguous sum
* [Concatenation of Array](./01_arrays_and_hashing/1929_concatenation_of_array.py) (Easy) - List concatenation
* [Fizz Buzz](./01_arrays_and_hashing/412_fizz_buzz.py) (Easy) - Classical modulo simulation

### 2. [Two Pointers](./02_two_pointers/)
* [Container With Most Water](./02_two_pointers/011_container_with_most_water.py) (Medium) - Inward two pointers with greedy area check
* [3Sum](./02_two_pointers/015_three_sum.py) (Medium) - Sort and two pointers
* [Remove Duplicates from Sorted Array](./02_two_pointers/026_remove_duplicates_from_sorted_array.py) (Easy) - Fast and slow pointers
* [Trapping Rain Water](./02_two_pointers/042_trapping_rain_water.py) (Hard) - Two pointers tracking max bounds
* [Merge Sorted Array](./02_two_pointers/088_merge_sorted_array.py) (Easy) - Three pointers from the end
* [Valid Palindrome](./02_two_pointers/125_valid_palindrome.py) (Easy) - Two pointers inwards
* [Two Sum II - Input Array Is Sorted](./02_two_pointers/167_two_sum_ii_input_array_is_sorted.py) (Medium) - Inward two pointers on sorted array

### 3. [Sliding Window](./03_sliding_window/)
* [Longest Substring Without Repeating Characters](./03_sliding_window/003_longest_substring_without_repeating_characters.py) (Medium) - Sliding window with hash set / direct address table
* [Longest Repeating Character Replacement](./03_sliding_window/424_longest_repeating_character_replacement.py) (Medium) - Dynamic sliding window tracking max frequency
* [Permutation in String](./03_sliding_window/567_permutation_in_string.py) (Medium) - Fixed-size sliding window with frequency delta
* [Minimum Window Substring](./03_sliding_window/076_minimum_window_substring.py) (Hard) - Dynamic sliding window with debt counter
* [Sliding Window Maximum](./03_sliding_window/239_sliding_window_maximum.py) (Hard) - Monotonic deque tracking window maximums
* [Best Time to Buy and Sell Stock](./03_sliding_window/121_best_time_to_buy_and_sell_stock.py) (Easy) - One-pass minimum tracking
* [Minimum Difference Between Highest and Lowest of K Scores](./03_sliding_window/1984_minimum_difference_between_highest_and_lowest_of_k_scores.py) (Easy) - Sort and contiguous window of size k

### 4. [Stack](./04_stack/)
* [Valid Parentheses](./04_stack/020_valid_parentheses.py) (Easy) - Stack matching with expected brackets
* [Evaluate Reverse Polish Notation](./04_stack/150_evaluate_reverse_polish_notation.py) (Medium) - Postfix evaluation with operand stack
* [Min Stack](./04_stack/155_min_stack.py) (Medium) - Constant-time getMin tracking via pair stack

### 5. [Binary Search](./05_binary_search/)
* [Median of Two Sorted Arrays](./05_binary_search/004_median_of_two_sorted_arrays.py) (Hard) - Binary search on partition
* [Binary Search](./05_binary_search/704_binary_search.py) (Easy) - Classic binary search
* [Search in Rotated Sorted Array](./05_binary_search/033_search_in_rotated_sorted_array.py) (Medium) - Pivot-guided binary search checking sorted half
* [Find Minimum in Rotated Sorted Array](./05_binary_search/153_find_minimum_in_rotated_sorted_array.py) (Medium) - Binary search with right bound comparison

### 6. [Linked List](./05_linked_list/)
* [Add Two Numbers](./05_linked_list/002_add_two_numbers.py) (Medium) - Column addition with carry
* [Merge Two Sorted Lists](./05_linked_list/021_merge_two_sorted_lists.py) (Easy) - Pointer merging with dummy head
* [Linked List Cycle](./05_linked_list/141_linked_list_cycle.py) (Easy) - Floyd's cycle detection
* [Reverse Linked List](./05_linked_list/206_reverse_linked_list.py) (Easy) - Iterative pointer reversal
* [Reorder List](./05_linked_list/143_reorder_list.py) (Medium) - Fast/slow middle finding, in-place reversal, and zipper merge
* [Merge k Sorted Lists](./05_linked_list/023_merge_k_sorted_lists.py) (Hard) - Sequential merge / divide and conquer / min-heap

### 7. [Trees](./07_trees/)
* [Same Tree](./07_trees/100_same_tree.py) (Easy) - Recursive comparison
* [Maximum Depth of Binary Tree](./07_trees/104_maximum_depth_of_binary_tree.py) (Easy) - DFS height
* [Balanced Binary Tree](./07_trees/110_balanced_binary_tree.py) (Easy) - Bottom-up height check
* [Invert Binary Tree](./07_trees/226_invert_binary_tree.py) (Easy) - Recursive swap
* [Diameter of Binary Tree](./07_trees/543_diameter_of_binary_tree.py) (Easy) - DFS max path

### 8. [Heap / Priority Queue](./08_heap_priority_queue/)
* [K Closest Points to Origin](./08_heap_priority_queue/973_k_closest_points_to_origin.py) (Medium) - Euclidean distance with min-heap
* [Kth Largest Element in a Stream](./08_heap_priority_queue/703_kth_largest_element_in_a_stream.py) (Easy) - Min-heap of size k
* [Last Stone Weight](./08_heap_priority_queue/1046_last_stone_weight.py) (Easy) - Max-heap with negated values

### 9. [Palindromes](./04_palindromes/)
* [Longest Palindromic Substring](./04_palindromes/005_longest_palindromic_substring.py) (Medium) - Expand around center
* [Palindromic Substrings](./04_palindromes/647_palindromic_substrings.py) (Medium) - Expand around center counting all valid palindromes

### 10. [Backtracking](./06_backtracking/)
* [Subsets](./06_backtracking/078_subsets.py) (Medium) - Decision tree generating power set
* [Letter Combinations of a Phone Number](./06_backtracking/017_letter_combinations_of_a_phone_number.py) (Medium) - Iterative expansion and recursion
* [Combination Sum](./06_backtracking/039_combination_sum.py) (Medium) - Decision tree with element reuse and undo
* [Word Search](./06_backtracking/079_word_search.py) (Medium) - 2D grid DFS backtracking with visited set
* [Word Search II](./06_backtracking/212_word_search_ii.py) (Hard) - Trie prefix tree combined with 2D grid backtracking

### 11. [Trie](./10_trie/)
* [Implement Trie (Prefix Tree)](./10_trie/208_implement_trie_prefix_tree.py) (Medium) - Prefix tree with insert, search, and startsWith
* [Design Add and Search Words Data Structure](./10_trie/211_design_add_and_search_words_data_structure.py) (Medium) - Trie with DFS wildcard matching for '.'

### 12. [Graphs](./11_graphs/)
* [Number of Islands](./11_graphs/200_number_of_islands.py) (Medium) - 2D grid Flood Fill (DFS sinking)
* [Clone Graph](./11_graphs/133_clone_graph.py) (Medium) - Deep copy of undirected graph using DFS and hash map

### 13. [Intervals](./09_intervals/)
* [Merge Intervals](./09_intervals/056_merge_intervals.py) (Medium) - Sort intervals by start time and merge overlaps
* [Insert Interval](./09_intervals/057_insert_interval.py) (Medium) - Binary insert and linear overlap merge

### 14. [Bit Manipulation](./12_bit_manipulation/)
* [Sort Integers by The Number of 1 Bits](./12_bit_manipulation/1356_sort_integers_by_the_number_of_1_bits.py) (Easy) - Hamming weight sorting via bit_count()

### 15. [1-D Dynamic Programming](./13_1d_dynamic_programming/)
* [Climbing Stairs](./13_1d_dynamic_programming/070_climbing_stairs.py) (Easy) - Fibonacci state transition with constant space
* [House Robber](./13_1d_dynamic_programming/198_house_robber.py) (Medium) - Recurrence with non-adjacent selection
* [House Robber II](./13_1d_dynamic_programming/213_house_robber_ii.py) (Medium) - Circular array subproblem reduction
* [Decode Ways](./13_1d_dynamic_programming/091_decode_ways.py) (Medium) - Forward bottom-up tabulation with single and double digit transitions
* [Coin Change](./13_1d_dynamic_programming/322_coin_change.py) (Medium) - Bottom-up unbounded knapsack with running minimum
* [Maximum Product Subarray](./13_1d_dynamic_programming/152_maximum_product_subarray.py) (Medium) - Kadane's variation tracking min and max bounds for sign flips
* [Word Break](./13_1d_dynamic_programming/139_word_break.py) (Medium) - Bottom-up suffix matching with dictionary validation
* [Longest Increasing Subsequence](./13_1d_dynamic_programming/300_longest_increasing_subsequence.py) (Medium) - O(n^2) DP checking all subsequent larger candidates

### 16. [2-D Dynamic Programming](./14_2d_dynamic_programming/)
* [Unique Paths](./14_2d_dynamic_programming/062_unique_paths.py) (Medium) - Grid path counting with space-optimized 1D row transition

---

## Running Tests

Each file includes test cases and can be run directly:

```bash
python3 01_arrays_and_hashing/001_two_sum.py
```
