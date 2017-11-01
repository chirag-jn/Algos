def merge(arr1,arr2):
	total1=len(arr1)
	total2=len(arr2)
	i=0
	j=0
	arr3=[]
	while (i<total1) and (j<total2):
		if(arr1[i]<=arr2[j]):
			arr3.append(arr1[i])
			i+=1
		elif(arr1[i]>arr2[j]):
			arr3.append(arr2[j])
			j+=1
	if(i==total1):
		arr3=arr3+arr2[j:]
	if(j==total2):
		arr3=arr3+arr1[i:]
	return arr3

def mergesort(A):
	if(len(A)==1):
		return A
	# L: first half
	# R: second half
	L=A[0:len(A)//2]
	R=A[len(A)//2:]
	l=mergesort(L)
	r=mergesort(R)
	a=merge(l,r)
	return a

arr=list(map(int,input().split()))
print(mergesort(arr))
