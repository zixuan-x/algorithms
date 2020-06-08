def find_string_anagrams(str, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  result_indices = []
  # Our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      # Decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):  # Have we found an anagram?
      result_indices.append(window_start)

    # Shrink the sliding window
    if window_end >= len(pattern) - 1:
      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1  # Before putting the character back, decrement the matched count
        char_frequency[left_char] += 1  # Put the character back

  return result_indices

from collections import Counter

def find_string_anagrams(str, pattern):
  result_indexes = []
  char_frequency = Counter(pattern)
  num_matched = 0
  window_start = 0

  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        num_matched += 1
    
    if num_matched == len(char_frequency):
      result_indexes.append(window_start)
    
    if window_end >= len(pattern) - 1:
      lelf_char = str[window_start]
      window_start += 1
      if char_frequency[lelf_char] == 0:
        num_matched -= 1
      char_frequency[lelf_char] += 1

  return result_indexes

