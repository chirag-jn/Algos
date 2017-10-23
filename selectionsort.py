arr=list(map(int,input().split()))
total=len(arr)
for i in range(total):
	minindex=arr.index(min(arr[i:]))
	temp=arr[i]
	arr[i]=arr[minindex]
	arr[minindex]=temp
print(arr)

# stable sort algo, inplace sorting algo
# inplace is based on how much extra space is being taken