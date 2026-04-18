#### 1. Import the numpy package under the name `np`
import numpy as np

#### 2. Print the numpy version and the configuration 

# print(np.__version__)
# np.show_config()

#### 3. Create a null vector of size 10 

# z = np.zeros(10)
# print(z)

#### 4. How to find the memory size of any array

# z = np.zeros((10,10))
# print("%d bytes" % z.nbytes)

#### 6. Create a null vector of size 10 but the fifth value which is 1

# z = np.zeros(10)

# z[4] = 1

# print(z)

#### 7. Create a vector with values ranging from 10 to 49 

# z = np.arange(10,50)

# print(z)

#### 8. Reverse a vector (first element becomes last)

# z = np.arange(50)
# z = z[::-1]
# print(z)

#### 9. Create a 3x3 matrix with values ranging from 0 to 8

# z = np.arange(9).reshape(3,3)
# print(z)

#### 10. Find indices of non-zero elements from [1,2,0,0,4,0]

# z = np.nonzero([1,2,0,0,4,0])
# print(z)

#### 11. Create a 3x3 identity matrix

# z = np.array([[1,0,0],[0,1,0],[0,0,1]])
# print(z)

# z = np.eye(3)
# print(z)

#### 12. Create a 3x3x3 array with random values

# z = np.random.random((3,3,3))
# print(z)

#### 13. Create a 10x10 array with random values and find the minimum and maximum values

# z = np.random.random((10,10))
# print(z.max())
# print(z.min())

#### 14. Create a random vector of size 30 and find the mean value

# z = np.random.random(30)

# print(z)
# print(z.mean())

#### 15. Create a 2d array with 1 on the border and 0 inside

# z = np.ones((5,5))

# z[1:-1,1:-1] = 0
# print(z)


#### 16. How to add a border (filled with 0's) around an existing array?

# z = np.ones((5,5))
# z = np.pad(z , pad_width=1 ,mode="constant",constant_values=0 )
# print(z)

#### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal 

# z = np.diag(1+np.arange(4) , k = -1)
# print(z)

#### 19. Create a 8x8 matrix and fill it with a checkerboard pattern 

# z = np.zeros((8,8))
# z[::2,::2] = 1
# z[1::2,1::2] = 1
# print(z)

#### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?

# z = np.ones((6,7,8))
# print(z)
# print(np.unravel_index(99,(6,7,8)))

#### 21. Create a checkerboard 8x8 matrix using the tile function 

# Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
# print(Z) 

#### 22. Normalize a 5x5 random matrix

# z = np.random.random((5,5))
# # normalized = (z - z.min()) / (z.max() - z.min())
# normalized = (z - np.mean(z)) / np.std(z)
# print(z)
# print(normalized)


#### 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA)


# color_dtype = np.dtype([("r" , np.ubyte),
#                         ("g" , np.ubyte),
#                         ("b" , np.ubyte),
#                          ("a" , np.ubyte) ])

# z = np.array([(255,0,0,255) , (0,255,0,128)],dtype=color_dtype)

# print(f"Data Type Is {z.dtype}")
# print(f"Red Channel of first pixel is: {z[0]['r']} ")

#### 24. Multiply a 5x3 matrix by a 3x2 matrix 

# z1 = np.ones((5,3))
# z2 = np.ones((3,2))

# result = np.matmul(z1 , z2)
# print(result)

# z = np.ones((5,3)) @ np.ones((3,2))
# print(z)

