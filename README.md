# Agcaoili_UrielJoseph_2ECEA_PA2

# ECE2112

NORMALIZATION PROBLEM

```python
import numpy as np   #Imports numpy

X = np.random.random((5,5))   #Generates a 5 by 5 array that stores random values of numbers
STD = X.std()   #Calculates the standard deviation of the elements in array "X" and stores the values in "STD"
M = X.mean()    #Calculates the mean of the elements in array X and stores the values in "M"
W = (X - M)   #Subtracts array "X" to array "M" and stores the value in "W"
Z = W/STD   #Divides array "W" to array "STD" to get the normalized array and stores the value in array "Z"

print("Normal Array: \n", X)   #Displays the randomly generated array
print("Normalized Array: \n", Z) #Displays the Normalized array
```
DIVISIBLE BY 3 PROBLEM

```python
import numpy as np   #Imports numpy

A = np.arange(1,101)   #Generates an array that consists of numbers 1 - 100 and stores it in "A"
np.shape(A)   #Declares the shape of array "A"
squares = A.reshape(10,10)**2   #Reshapes array "A" to 10 x 10 while getting the square of each element in the array and storing the value in "squares"
divby3 = squares[squares%3==0]   #Takes the moldulus of squares and only takes the values that returns the remainder 0 and stores it in "divby3"

print("Array 10 x 10: \n", squares)   #Displays the array which stores the squares of each element from the original array
print("Numbers that are divisible by 3: \n", divby3)   #Displays the array which stores the elements that are divisible by 3
```
