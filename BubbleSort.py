#bubblesort
#compare adjacent values and interchange

A=[]
for u in range(8):
    A.append(int(input("Enter a number: ")))
print(A)

def bubbleSort(A):
    for i in range(1, len(A)):
        for j in range(1, len(A)-i+1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
            
bubbleSort(A)
print(A)
