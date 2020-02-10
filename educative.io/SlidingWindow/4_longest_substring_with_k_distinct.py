def longest_substring_with_k_distinct(str, k):
    max_len = float("-inf")
    c_dict = {}
    window_start = 0
    for window_end in range(len(str)):
        c = str[window_end]
        c_dict[c] = c_dict[c] + 1 if c in c_dict else 1
        while len(c_dict) > k and window_start <= window_end:
            temp = str[window_start]
            if c_dict[temp] == 1:
                del c_dict[temp]
            else:
                c_dict[temp] -= 1
            window_start += 1
        max_len = max(max_len, window_end - window_start + 1) 

    return int(max_len) if max_len != float("-inf") else 0

def longest_substring_with_k_distinct(str, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
      left_char = str[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length
