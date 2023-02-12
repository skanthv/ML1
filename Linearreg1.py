#'''
#version 1
import numpy as np
#to represent rows and cols type of data for basic purpose ..need functions to allow data manipulaation on it
# ..so need numpy library
#numpy library has code for arrays and matrices

x=np.array([[1],[2],[3],[4]])
#array function should have 1 parameter i.e a list..
# inside it you can have any number of lists..that is the number of rows in this array..
# in each list that represents a row item, how many values are there indicates the number of columns
#so this has 4 lists in the outside list..so 4 rows.. in each of those 4 lists..theer i 1 element,so 1 column.

print(x)
y=np.array([2,3,4,5])
#in this main list, there are no smaller lists.. so just 1 row
#in that 1 row..there are 4 numbers.. so 4 columns..

print(y)
from sklearn.linear_model import LinearRegression
#sklearn is a module with all classical machine learning classes..
#linear_model module implements all linear methods
#LinearRegression is a class for ORDINARY LEAST SQUARES REGRESSION Technique


reg=LinearRegression().fit(x,y)
y_pred=reg.predict([[6]])
print("predicted value is ",y_pred)
#'''
print("Coefficients are=",reg.coef_) #coeff of independent variables estimated
print("R squaread=",reg.score(x,y)) # r squared value i.e. coeff of determination

