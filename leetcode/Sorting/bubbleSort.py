# Sorts a sequence in ascending order using the bubble sort algorithms.
def bubbleSort(arr):
	n = len(arr)
	# Perform n-1 bubble operations on the sequence.
	for i in range(n - 1):
		# Bubble the largest item to the end.
		for j in range(n - 1 - i):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j] 

arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)