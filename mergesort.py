def mergeSort(arr):
	if len(arr)>1:
		mid = len(arr)//2
		lefthalf = arr[:mid]
		righthalf = arr[mid:]
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				arr[k]=lefthalf[i]
				i=i+1
			else:
				arr[k]=righthalf[j]
				j=j+1
			k=k+1
		while i < len(lefthalf):
			arr[k]=lefthalf[i]
			i=i+1
			k=k+1
		while j < len(righthalf):
			arr[k]=righthalf[j]
			j=j+1
			k=k+1

arr=list(map(int,input().split()))
mergeSort(arr)
print(arr)

# its a stable sort, not an inplace sorting algo
# in inplace sorting, extra space is constant
# here extra space is total1+total2
# so, extra space depends on problem size

# merge sort can also work as a helper function, by dividing the lists into two both of which are sorted
