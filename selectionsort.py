arr=list(map(int,input().split()))
total=len(arr)
for i in range(total):
	mintemp=min(arr[i:])
	minindex=arr.index(mintemp)
	temp=arr[i]
	arr[i]=arr[minindex]
	arr[minindex]=temp
print(arr)