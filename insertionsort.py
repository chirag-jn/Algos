arr=list(map(int,input().split()))
total=len(arr)
for i in range(1,total):
	j=i-1
	temp=arr[i]
	while j>=0 and temp<arr[j]:
		arr[j+1]=arr[j]
		j-=1
	arr[j+1]=temp	
print(arr)
