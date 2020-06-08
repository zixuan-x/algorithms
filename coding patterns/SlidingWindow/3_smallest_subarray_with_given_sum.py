def smallest_subarray_with_given_sum(s, arr):
  window_sum, min_len = 0, float("inf")
  window_start = 0
  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s and window_start <= window_end:
      min_len = min(min_len, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
  return int(min_len) if min_len != float("inf") else 0