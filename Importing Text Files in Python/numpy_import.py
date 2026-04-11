import numpy as np

sample_array = np.array([0, 0, 7])
print(type(sample_array))
print("Size: %d" % sample_array.size)
print("Shape: %d" % sample_array.shape)
print(sample_array, "\n")

nested_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(nested_array))
print("Size: %d" % nested_array.size)
print("Shape: %s" % str(nested_array.shape))
print(nested_array, "\n")

all_zeros = np.zeros((3, 3))
print(type(all_zeros))
print(all_zeros, "\n")
print(all_zeros)


unitialized = np.empty((2, 2))
print(unitialized, "\n")

print(nested_array)
print(nested_array.flatten(), "\n")

range_value = np.arange(10)
print(range_value, "\n")    

# Creates a 1D array with values from 1 to 10
ranged_values_two = np.arange(1, 11)
print(ranged_values_two, "\n")

# Creates a 1D array with values from 0 to 1 in increments of 0.1
arranged_increment = np.arange(0, 1, 0.1)
print(arranged_increment, "\n")

# Import a NumPy text file
badges_saved_np = np.loadtxt('Importing Text Files in Python/badges-five-numpy.txt')
print(badges_saved_np, "\n")

# Import a comma separated file
# It is required to specify delimiter, else an exception is raised
try:
    badges_comma = np.loadtxt('Importing Text Files in Python/badges-five.txt') # error
except Exception as e:
    print(str(e))

badges_comma = np.loadtxt('Importing Text Files in Python/badges-five.txt', delimiter=',')
print(badges_comma, "\n")

# Import a comma separated file that has a header row
# Error occurs, unless I skip the header row
try:
    badges_header = np.loadtxt('Importing Text Files in Python/badges-five-header.txt', delimiter=',', skiprows=1)
except Exception as e:
    print(str(e))