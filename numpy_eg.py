# numpy - numerical python
# mathematical functions for arrays and matrices
# handle multidimensional data
# pip install numpy

import numpy as np

a = np.array([[1,2],[3,4]])  # create a 2D array 2X2 
b = np.array([[5,6],[7,8]])  # create another 2D array 2X2

# 3 X 4
c = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])  # create a array 3X4
allzero_array = np.zeros((4,3))
print(allzero_array)
allOnes_array = np.ones((2,2))
print(allOnes_array)
d = np.arange(0,10,3)
print(d)  # create an array with values from 0 to 9
e = np.linspace(0,1,5)
print(e)

print(d.shape)


f = np.array([[2,3,4,6],[4,5,6,6]])  # create a 2D array with shape (1,2)
print(f.shape)  # print the shape of the array

d1 = np.arange(0,10,2)  # create an array with values from 0 to 9 with step 2
print(d1)
print(d1.shape)
print(d1.ndim)

d2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]       
])


print(d2)
print(d2.shape)  # print the shape of the array
print(d2.ndim)  # print the number of dimensions of the array
print(d2.size)  # print the number of elements in the array


d2 = np.arange(9)
print(d2)
print(d2.shape)
print(d2.ndim)
d3 = d2.reshape(3,3)
print(d3)
print(d3.shape)  # print the shape of the reshaped array
print(d3.ndim)  # print the number of dimensions of the reshaped array


d2 = np.arange(10).reshape(2,5)  # create an array with values from 0 to 9 and reshape it to 2X5
print(d2)
print(d2.shape)  # print the shape of the array
print(d2.ndim)

d3 = np.arange(27).reshape((3,3,3))
print(d3)
print(d3.shape)  # print the shape of the 3D array
print(d3.ndim)  # print the number of dimensions of the 3D array4

d1 = np.array([1,2,3,4,5,6])
d2 = d1.reshape(2,3)  # reshape the 1D array to a 2D array with shape (2,3)
print(d2)
"""
    0 1  2
0   1 2  3
1   4 5  6
2   7 8  9


to access 5 -> arr[1,1]
"""
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1,1])
print(arr[:,0]) 
print(arr[:,1]) 
print(arr[:,2]) 

print(arr[2:3, :])# access rows 1 to 2 and all columns])

a = np.array([1,2,3])
b = np.array([10,20,30])

print(a+b)

a2 = np.arange(0,8).reshape(2,4)  # create a 2D array with values from 0 to 7
b2 = np.arange(8,16).reshape(2,4)  # create another 2D array with values from 8 to 15
print(a2)
print(b2)
# multiplication = a2 * b2  # element-wise multiplication
m2 = a2 * b2
print(m2)  # print the result of element-wise multiplication

print(a2 ** 3)
print(np.sqrt(a2))


arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr)
# total sum of all elements
print(np.sum(arr))  # sum of all elements
# mean value of all elements
print(np.mean(arr))  # mean value of all elements
print(np.max(arr))  # maximum value of all elements
print(np.min(arr))  # minimum value of all elements
print(arr)
print(np.sum(arr, axis=0))  # sum of each column
print(np.sum(arr, axis=1))  # sum of each row

# transpose of the array
print(arr)
print(arr.T)  # transpose of the array

arr1 = np.random.randint(0, 100, (3, 3))  # create a random array with shape (3,3)
print(arr1)


a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

# matrix multiplication
print(a)
print(b)
c = np.dot(a, b)  # matrix multiplication
print(c)  # print the result of matrix multiplication


a = np.array([1,2,3,4,5,6])
print(a)
a = np.add(a, 10)  # add 10 to each element of the array
print(a)
a = np.subtract(a,10)  # subtract 10 from each element of the array
print(a)
a = np.multiply(a, 10)  # multiply each element of the array by 10
print(a)
a = np.divide(a, 10)  # divide each element of the array by 10
print(a)
a = np.power(a, 2)  # raise each element of the array to the power of 2
print(a)  # print the result of raising each element to the power of 2
a = np.mod(a,3)
print(a)  # print the result of taking the modulus of each element with 3
a = np.log(a)
print(a)

arr = np.array([[1,2,3,4,5,6], [7,8,9,10,11,12]])
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))

arr = np.random.randint(0, 100, (3, 3))  # create a random array with shape (3,3)
print(arr)
print(np.sort(arr))  # sort the array
print(np.argsort(arr))  # get the indices that would sort the array
print("Array:",arr)

arr = np.random.randint(0, 20, (3, 3))  # create a random array with shape (3,3)
print("Array:",arr)
print(np.where(arr > 10, 1, 0))  # replace values greater than 10 with 1 and others with 0

