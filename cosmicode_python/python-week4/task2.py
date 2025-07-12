def multiplication():
    row1=int(input("Enter the number of rows for 1st matrix: "))
    col1=int(input("Enter the number of columns for 1st matrix: "))
    row2=int(input("Enter the number of rows for 2nd matrix: "))
    col2=int(input("Enter the number of columns for 2nd matrix: "))
    if col1!=row2:
        print("The input values aren't coorect for muliplication")
        return
    print("Matrix 1 data")
    matrix1_col=[]
    for i in range(row1):
        matrix1_row=[]
        for j in range(col1):
            matrix1_row.append(int(input("Enter the number: ")))
        matrix1_col.append(matrix1_row)
    print("Matrix 2")
    matrix2_col=[]
    for i in range(row2):
        matrix2_row=[]
        for j in range(col2):
            matrix2_row.append(int(input("Enter the number: ")))
        matrix2_col.append(matrix2_row)
    multiplied_col=[]
    for i in range(row1):
        multiplied_row=[]
        for j in range(col2):
            val=0
            for k in range(col1):
                val+=matrix1_col[i][k]*matrix2_col[k][j]
            multiplied_row.append(val)
        multiplied_col.append(multiplied_row)
    print("Multiplied result\n")
    for i in range(row2):
        for j in range(col1):
            print(multiplied_col[i][j], end=" ")
        print("\n")

multiplication()

