# Source: CodeWithHarry via Youtube
# URL: https://www.youtube.com/watch?v=6kYUo2FSBFo

# Adding Two Matrices using Python 

def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp1 = int(input(f"Enter O[{i}][{j}]"))
            row.append(inp1)
        o.append(row)
    return o

def sum(A, B):
    output = []
    for i in range(len(A)): #Number of rows
        row = []
        for j in range(len(A[0])): #Number of columns
            row.append(A[i][j] + B[i][j])
        output.append(row)
    return output

m = int(input("Enter the value of m\n"))
n = int(input("Enter the value of n\n"))

print("Enter Matrix A")
A = matrix(m, n)
print(A)

print("Enter Matrix B")
B = matrix(m, n)
print(B)

s = sum(A, B)
print("Sum of Matrices =", s)

# Additional Comments
#   Takeout Matrix
#      > [1, 2, 3, 5, 6]
#      > [1, 3, 3, 7, 9]