matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a=raw_input("enter element 1 ")
b=raw_input("enter element 2 ")
c=raw_input("enter element 3 ")
d=raw_input("enter element 4 ")

matrix_min=[[int(a),int(b)],[int(c),int(d)]]

for i in range(4):
	for j in range(4):
		
		if  matrix[i][j]== matrix_min[0][0]:
			if (matrix[i+1][j+1] == matrix_min[1][1]) and (matrix[i][j+1] == matrix_min[0][1]) and ( matrix[i+1][j] == matrix_min[1][0] ):
				print "row:{0}\ncol:{1}".format(i,j)
