# Name: sidra ahmad
# Student ID: 202410055

import numpy as np

# given array
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# 1. third row, first column
print("1:", arr[2, 0])

# 2. second column
print("2:", arr[:, 1])

# 3. data type
print("3:", arr.dtype)

# 4. copy
arr_copy = arr.copy()
arr_copy[0, 0] = 999
print("4 - original:", arr)
print("4 - copy:", arr_copy)

# 5. view
arr_view = arr.view()
arr_view[0, 0] = 555
print("5 - original after view:", arr)

# 6. shape
print("6:", arr.shape)

# 7. loop with position
print("7:")
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(f"Element {arr[i,j]} at row {i}, column {j}")

# 8. join arrays
new_arr = np.ones((3,3))
print("8 - vertical join:\n", np.vstack((arr, new_arr)))
print("8 - horizontal join:\n", np.hstack((arr, new_arr)))

# 9. split by columns
print("9:", np.hsplit(arr, 3))

# 10. position of value 60
print("10:", np.where(arr == 60))

# 11. sort each row
print("11:\n", np.sort(arr))

# 12. elements greater than 50
print("12:", arr[arr > 50])

# 13. random 2x3 array
rand_arr = np.random.randint(1, 101, (2,3))
print("13:\n", rand_arr)

# 14. numpy ufunc
print("14 - add 5:\n", np.add(arr, 5))
