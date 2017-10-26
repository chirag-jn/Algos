# in selection sort, loop starts from 0
# we find the min element in rest of list including the current element
# and then swap the current element with the min element

arr=list(map(int,input().split()))
total=len(arr)
for i in range(total):
	least=i
	for k in range(i+1,total):
		if(arr[k]<arr[least]):
			least=k
	temp=arr[i]
	arr[i]=arr[least]
	arr[least]=temp
print(arr)

# stable sort algo, inplace sorting algo
# inplace is based on how much extra space is being taken