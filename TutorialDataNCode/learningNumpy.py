import numpy as np

### 1. normal array
# a = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# print(a[3:6])
# print(a[3:6:2]) 

### 2. numpy array
# b = np.array(a)
# print(b)
# print(b[3:6])
# print(b[3:6:2])

### 3. numpy multidimensional array
# aMulti = np.array([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]) # 2 rows, 10 columns, it' mandatory to have the same number of elements in each row
# print(aMulti)
# print(aMulti[1,3])
# print(aMulti[0:,3:6])
# print(aMulti.shape) # returns the shape of the array (rows, columns) also called the dimension of the array
# print(aMulti.ndim) # returns the number of dimensions of the array
# print(aMulti.size) # returns the number of elements in the array
# print(aMulti.dtype) # returns the data type of the array

### 4. numpy array creation
# a = np.full((2,3,4), 5) # creates a 3D array with 2 rows, 3 columns and 4 elements in each row, all elements are 5
# print(a)
# a = np.zeros((2,3,4)) # creates a 3D array with 2 rows, 3 columns and 4 elements in each row, all elements are 0
# print(a)
# a = np.zeros_like(a) # creates a 3D array with 2 rows, 3 columns and 4 elements in each row, all elements are 0, the shape of the array is the same as the array passed as parameter
# print(a)

### 5. numpy array creation with generator functions
# a = np.arange(10) # creates an array with 10 elements, the elements are 0,1,2,3,4,5,6,7,8,9
# print(a)
# a = np.arange(0,1000,5) # creates an array with elements from 0 to 1000 with a step of 5
# print(a) # [  0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90  95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195 200 205 210 215 220 225 230 235 240 245 250 255 260 265 270 275 280 285 290 295 300 305 310 315 320 325 330 335 340 345 350 355 360 365 370 375 380 385 390 395 400 405 410 415 420 425 430 435 440 445 450 455 460 465 470 475 480 485 490 495 500 505 510 515 520 525 530 535 540 545 550 555 560 565 570 575 580 585 590 595 600 605 610 615 620 625 630 635 640 645 650 655 660 665 670 675 680 685 690 695 700 705 710 715 720 725 730 735 740 745 750 755 760 765 770 775 780 785 790 795 800 805 810 815 820 825 830 835 840 845 850 855 860 865 870 875 880 885 890 895 900 905 910 915 920 925 930 935 940 945 950 955 960 965 970 975 980 985 990 995]
# a = np.linspace(0,1000,5) # creates an array with 5 elements from 0 to 1000
# print(a) # [   0.  250.  500.  750. 1000.]

### 6. numpy array creation with random numbers
# a = np.random.rand(2,3) # creates a 2D array with 2 rows and 3 columns, the elements are random numbers between 0 and 1
# print(a)
# a = np.random.randint(0,100,10) # creates an array with 10 elements, the elements are random numbers between 0 and 100
# print(a)

### 7. nan and inf
# print(np.nan) # nan
# print(np.inf) # inf
# print(np.NINF) # -inf
# print(np.isnan(np.nan)) # True
# print(np.isinf(np.inf)) # True
# print(np.isfinite(np.inf)) # False
# print(np.isfinite(np.nan)) # False

### 8. sqrt
# np.sqrt(4) # 2.0
# np.sqrt(-1) # nan
# np.sqrt(np.inf) # inf
# np.sqrt(np.nan) # nan


### 9. numpy math operations on arrays
# print(np.array([2,4,6,8,10]) + 2) # [ 4  6  8 10 12]
# print(np.array([2,4,6,8,10]) - 2) # [0 2 4 6 8]
# print(np.array([2,4,6,8,10]) * 2) # [ 4  8 12 16 20]
# print(np.array([2,4,6,8,10]) / 2) # [1.  2.  3.  4.  5. ]
# print(np.array([2,4,6,8,10]) // 2) # [1 2 3 4 5]
# print(np.array([2,4,6,8,10]) % 2) # [0 0 0 0 0]
# print(np.array([2,4,6,8,10]) + np.array([2,4,6,8,10])) # [ 4  8 12 16 20]

### 10. array operations
# a = np.array([1,2,3])
# print(a) # [1 2 3]
# a = np.append(a, [7,8,9])
# print(a) # [1 2 3 7 8 9]
# a = np.insert(a, 3, [4,5,6])
# print(a) # [1 2 3 4 5 6 7 8 9]

### 11. array operations - delete
# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a) # [1 2 3 4 5 6 7 8 9]
# print(np.delete(a, [0,1,2])) # deletes the elements at index 0,1,2
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print("-----------------------------------------------------------")
# print(np.delete(a, 0, 0)) # deletes the row at index 0
# print("-----------------------------------------------------------")
# print(np.delete(a, 0, 1)) # deletes the column at index 0
# print("-----------------------------------------------------------")
# print(np.delete(a, [0,1], 0)) # deletes the rows at index 0 and 1

### 12. array operations - reshape
# a = np.array([[0,1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19]])
# print(a.shape) # (2, 10)
# print(a.reshape(10,2)) # reshapes the array to 10 rows and 2 columns
# print(a.reshape(5,2,2)) # reshapes the array to 5 rows, 2 columns and 2 depth
# print(a.reshape(20,)) # reshapes the array to 20 rows and 1 column
 # _-_ using resize hase the same effect as reshape but it changes the original array _-_
 