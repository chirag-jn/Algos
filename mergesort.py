# precondition, the two lists which are inputs are already sorted
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
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
print(arr3)

# its a stable sort, not an inplace sorting algo
# in inplace sorting, extra space is constant
# here extra space is total1+total2
# so, extra space depends on problem size