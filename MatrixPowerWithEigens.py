import sympy as sym

A = sym.Matrix([[0, 1], [1, 1]])
M = sym.Matrix([[2, 2], [1+sym.sqrt(5), 1-sym.sqrt(5)]])
M_inv = M ** (-1)

print(f"Linear Transformation matrix, A = {A}")
print(f"Change of basis matrix, M = {M}\n")

diagonalMat = sym.simplify(M_inv*A*M)
print(f"STEP1: Translate A to eigen basis: daiagonalMat = M_inv . A . M = {diagonalMat}\n")

poweredDiagonalMat = sym.simplify(diagonalMat**3)
print(f"STEP2: calculate daiagonalMat^3 which is a lot easier,  poweredDiagonalMat = {poweredDiagonalMat}\n")

print("STEP3:This is equal to (M_inv . A^3 . M). So, to solve for A^3, translate poweredDiagonalMat to our coordinate system, ")
print(f"(M . poweredDiagonalMat . M_inv) = {sym.simplify(M * poweredDiagonalMat * M_inv)}\n")

print(f"Actual A^3 = ", A**3)