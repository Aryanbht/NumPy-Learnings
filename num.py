import numpy as np 

# array = np.array([[[1,2,3],[1,2,3],[1,2,3]],
#                  [[1,2,3],[1,2,3],[1,2,3]],
#                  [[1,2,3],[1,2,3],[1,2,3]]])

# print(array.ndim)
# print(array.shape)
# print(array[2,2,1])

#*1.Slicing
# array = np.array([[1,2,3,4,],
#                   [5,6,7,8,],
#                   [9,10,11,12],
#                   [13,14,15,16]])
# print(array.ndim)
# print(array.shape)
#*Row Selection  
#array[start:end:step]

# print(array[0:4:2])
# print(array[0:3:2])
# print(array[::-1])

#*Column Selection

# print(array[:,0])
# print(array[:,0:4])
# print(array[:,1:3])
# print(array[:,::2])
# print(array[0:2,0:2])
# print(array[2:3,1:3])

# *Arthematic Operation 

#*Scaler 

# array = np.array([1,2,3])

# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array / 2)
# print(array ** 5)

#*Vector 

# array = np.array([1.09,2.87,3.45])

#  print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array)) #round down 
# print(np.ceil(array)) #round up

# print(np.pi)

# *problem 1 : Convert radii to Areas 

# radii = np.array([2,4,6])

# print(np.pi * radii**2)

# *Element Wise Arthematic

# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1 + array2) 
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 ** array2)

#*Comparision Operators

# score = np.array([45,65,88,20,99])

# print(score == 100)
# print(score >= 50)
# print(score <= 50)

# score[score < 30] = 0
# print(score)










