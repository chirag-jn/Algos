arr=list(map(int,input().split()))
total=len(arr)
for i in range(total): # this loop statement helps only in traversing from end.
	# we can also do: for i in range(total-1,-1,-1):
	# then the next loop will also change
	# below comment explains this only.
	# considering that last i elements are already sorted
	for j in range(0,total-i-1):
		if(arr[j]>arr[j+1]):
			arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

		
