# Example 3x3 matrices A and B

A=[ [5,3,-2] , [1,0,7], [-6,2,0] ]

B=[ [6,1,4] , [0,1,3] , [0,-1,7] ]

# Create matrix C with the differences A[i][j] - B[i][j]
C = []
for i in range(3):
    row = []
    for j in range(3):
        diff = A[i][j] - B[i][j]
        row.append(diff)
    C.append(row)

# Print result
print("Matrix C (A - B):")
print(C)