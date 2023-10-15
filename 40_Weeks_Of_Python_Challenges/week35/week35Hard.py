# Date: 7/28/2023
# Author: Shantel Williams

# Hard:
# Given the following numpy array, data, write a Python program to remove outliers using the Z-score method. data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100])
# Notes: Outliers are data points that are too far away from other data points. 
# Z-scores are the number of standard deviations above and below the mean decrease for each value. Z score = (x -mean) / std. deviation
# If the z score of a data point is more than 3, it indicates that the data point is quite different from the other data points. Such a data point can be an outlier.
import numpy as np 
####################

def remove_outliers(numpy_array):
    if len(numpy_array) == 0:   # if empty array is passed. 
        return "Empty array was provided."
    
    mean = np.mean(numpy_array) # returns the mean
    standard_deviation = np.std(numpy_array) #returns the std. deviation
    outlier_data_point = 3 # z score over three is considered an outlier.
    number = 0 # variable track index
    outliers = [] # list to hold all of the outliers
    updated_array = [] # list that I will return after removing outliers
    
    while number < len(numpy_array): # looping through each number
        #Z score = (x -mean) / std. deviation
        z = (numpy_array[number] - mean) / standard_deviation # formual to find z score
        if z > outlier_data_point or z  < -outlier_data_point: # if z score is higher than 3
            outliers.append(numpy_array[number]) # add that as a outlier
        number+=1 # increment count 

    for outliner in outliers: # grab the stored outliers and delete them. 
        updated_array = np.delete(numpy_array, np.where(numpy_array == outliner)) # returns a new array with the outliers removed

    return updated_array

def main():
    # provided test case and a few extra
    test = remove_outliers(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]))
    test2 = remove_outliers(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -500]))
    test3 = remove_outliers(np.array([]))
    print(test)
    print(test2)
    print(test3)
    
main()
