"""
Matrix Rank Calculator
Name: Chirag Jain
"""
from copy import deepcopy

def swapRows(A,row1,row2):
	# A is the Matrix
	# row1 and row2 are the indexes of rows to swap
	temp=list(A[row1])
	A[row1]=list(A[row2])
	A[row2]=list(temp)
	return A
	
def Row_Transformation(A,x,row1,row2):
	# A is the Matrix
	# Formula used: A[row2]=A[row2] + x*A[row1]
	temp=deepcopy(A[row1])
	for i in range(len(temp)):
		temp[i]=temp[i]*x
		A[row2][i]+=temp[i]
	return A

def MatrixRank(A):
	rank=len(A[0])
	rank=min(len(A),len(A[0]))
	for row in range(0,min(len(A),len(A[0]))):
		if(A[row][row]!=0):
			for temp in range(0,len(A)):
				if(temp!=row):
					A=deepcopy(Row_Transformation(A,(-1)*(A[temp][row]/A[row][row]),row,temp))
		else:
			flag=0
			for j in range(row+1,len(A)):
				if(A[j][row]!=0):
					A=deepcopy(swapRows(A,j,row))
					flag=1
					break
			if(flag==0):
				rank-=1
				A=deepcopy(swapRows(A,row,len(A)-1))
	return rank
	
def matrixinput():
	A=[]
	rows=int(input('Enter Number of Rows: '))
	cols=int(input('Enter Number of Columns: '))
	if (rows<=0 or cols<=0):
		print("Matrix Doesn't exist")
		return
	for i in range(rows):
		A.append(list(map(float,input().split())))
	print(MatrixRank(A))
	print("Final Matrix: ")
	for i in range(rows):
		print(A[i])

matrixinput()
