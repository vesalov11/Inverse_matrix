import numpy as np

# Въвеждане на размера на матрицата (n)
n = int(input("Въведете размера на квадратната матрица (n): "))

# Въвеждане на стойностите на елементите на матрицата
matrix = []

print(f"Въведете {n} реда по {n} стойности за матрицата:")

for i in range(n):
    ред = []
    for j in range(n):
        стойност = float(input(f"Въведете елемент ({i+1},{j+1}): "))
        ред.append(стойност)
    matrix.append(ред)

# Смятане на обратната матрица
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Обратната матрица е:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("Матрицата няма обратна матрица.")
