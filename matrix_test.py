A=[ [5,3,-2] , [1,0,7] ]
B=[ [6,1] , [0,1] , [0,-1] ]

A.append([A[0][i] + A[1][i] for i in range(3)])
B=[[B[j][0], B[j][1], B[j][0]+B[j][1]] for j in range(3)]
print(A,B)