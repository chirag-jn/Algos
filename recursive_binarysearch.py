def binarysearch(arr,x,l,r):
	mid=(l+r)//2
	if(r<l):
		return -1
	if(arr[mid]==x):
		return mid
	elif(arr[mid]>x):
		return binarysearch(arr,x,l,mid-1)
	elif(arr[mid]<x):
		return binarysearch(arr,x,mid+1,r)

arr = list(map(int,input("Enter Array: ").split()))
elem = int(input("Enter Number to search: ")) 
print(binarysearch(arr,elem,0,len(arr)-1))