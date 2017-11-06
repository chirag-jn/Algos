arr=list(map(int,input().split()))
total=len(arr)
for i in range(total):
	# considering that last i elements are already sorted
	for j in range(0,total-i-1):
		if(arr[j]>arr[j+1]):
			arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

		