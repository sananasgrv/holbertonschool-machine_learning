#!/usr/bin/env python3
"""7-main.py"""

cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D

# ======================
# TEST 1 (axis = 0, empty mat2)
# ======================
mat1 = [[1], [2]]
mat2 = []
print(cat_matrices2D(mat1, mat2))

# ======================
# TEST 2 (axis = 0, normal)
# ======================
mat1 = [
    [4, -7, 56, 2],
    [5, 106, 7, 2],
    [2, -6, 3, 23],
    [0, -6, 3, 42]
]
mat2 = [[73, 8, 2, 99]]
print(cat_matrices2D(mat1, mat2))

# ======================
# TEST 3 (axis = 0, bigger values)
# ======================
mat1 = [
    [484, 247, -556],
    [554, 16, 75],
    [5, 88, 23],
    [233, -644, 325]
]
mat2 = [[406, -16, 33]]
print(cat_matrices2D(mat1, mat2))

# ======================
# TEST 4 (axis = 1)
# ======================
mat1 = [
    [-54, -87, 56, -92, 81, 12],
    [54, 16, -72, 42, 901, -10]
]
mat2 = [
    [63],
    [69]
]
print(cat_matrices2D(mat1, mat2, axis=1))

# ======================
# EXTRA: shape mismatch tests (should print None)
# ======================
print(cat_matrices2D([[1, 2]], [[3]], axis=0))
print(cat_matrices2D([[1, 2]], [[3, 4], [5, 6]], axis=1))
