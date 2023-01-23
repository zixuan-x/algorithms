def mergeSort(arr):
	if not arr or len(arr) < 2:
		return
	recMergeSort(arr, 0, len(arr) - 1)	

def recMergeSort(arr, left, right):
	if left >= right:
		return
	mid = (left + right) // 2
	recMergeSort(arr, left, mid)
	recMergeSort(arr, mid + 1, right)
	merge(arr, left, mid + 1, right)

def merge(arr, start1, start2, end):
	L = arr[start1 : start2]
	R = arr[start2 : end + 1]
	
	n1 = len(L)
	n2 = len(R)
	i, j, k = 0, 0, start1
	
	while i < n1 and j < n2:
		if L[i] < R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

arr = [12, 11, 13, 5, 6, 7] 
mergeSort(arr)
print(arr)