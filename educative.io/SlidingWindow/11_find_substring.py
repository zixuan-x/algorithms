from collections import Counter

def find_substring(str, pattern):
  window_start, matched, substr_start = 0, 0, 0
  min_length = len(str) + 1
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      char_frequency[right_char] -= 1
      if char_frequency[right_char] >= 0:  # Count every matching of a character
        matched += 1

    # Shrink the window if we can, finish as soon as we remove a matched character
    while matched == len(pattern):
      if min_length > window_end - window_start + 1:
        min_length = window_end - window_start + 1
        substr_start = window_start

      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        # Note that we could have redundant matching characters, therefore we'll decrement the
        # matched count only when a useful occurrence of a matched character is going out of the window
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  if min_length > len(str):
    return ""
  return str[substr_start:substr_start + min_length]

def find_substring(str, pattern):
  char_frequency = Counter(pattern)
  num_matched = 0
  window_start = 0
  res = []

  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in char_frequency:
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        num_matched += 1
  
    while num_matched == len(char_frequency):
      res.append([window_start, window_end])
      left_char = str[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          num_matched -= 1
        char_frequency[left_char] += 1
  
  if res:
    index = 0
    for i in range(1, len(res)):
      if res[i][1] - res[i][0] + 1 < res[index][1] - res[index][0] + 1:
        index = i
    return str[res[index][0]:res[index][1] + 1]
  else:
    return ""