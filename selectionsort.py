# in selection sort, loop starts from 0
# we find the min element in rest of list including the current element
# and then swap the current element with the min element

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