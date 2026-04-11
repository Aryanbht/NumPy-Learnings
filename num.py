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
#*Broadcasting 
#! We can Broadcast Two arrays when checking from left two right no. are same or one of them is one. 
# arr1 =  np.array([[1,2,3,4]])
# arr2 = np.array([[1],[2],[3],[4]])

# print(arr1.shape)
# print(arr2.shape)

# print(arr1 * arr2)

#*Aggregate Function

# array = np.array([[1,2,3,4,5],
#                   [6,7,8,9,10]]) 

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))
# print(np.sum(array , axis = 0))
# print(np.sum(array , axis = 1))

#*Filtering 


# ages = np.array([[5,6,4,32,78],
#                 [9,3,54,21,56]])

# teens = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages <=65) ]
# print(teens)
# print(adults)

# adult = np.where(ages > 18 , ages , "-")
# print(adult)

#*Random Numbers 

# rng = np.random.default_rng()

# print(rng.integers(low = 0 , high = 100 , size = (3,2,3)))
# np.random.seed(seed=1)
# print(np.random.uniform(low= -1 , high = 2 , size=(3,2)))


# rng = np.random.default_rng()
# arr = np.array([2,3,8,9])
# rng.shuffle(arr)
# print(arr)
# arr1 = rng.choice(arr , 3)
# print(arr1)

