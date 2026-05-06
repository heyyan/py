import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

print(arr1)
print(arr2)

print(f"Horizontal Stack:{np.hstack((arr1, arr2))} ")
print(f"Vertical Stack:{np.vstack((arr1, arr2))} ")
print(f"Depth Stack:{np.dstack((arr1, arr2))}")
