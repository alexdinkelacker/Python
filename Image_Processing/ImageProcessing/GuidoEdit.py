'''
Created on Apr 1, 2020

@author: alexd
'''
print('P2.4 page 80 Integer Calculation:')
int1 = int(input('Enter integer 1'))
int2 = int(input('Enter integer 2'))
print('\nThe sum is: ', int1 + int2)
print('\nThe differnece is: ', int1-int2, '\n')
print('The product is: ', int1*int2, '\n')
print('The average is: ', (int1+int2)/2, '\n')
print('The distance (absolute value of the difference): ', abs(int1-int2), '\n')
print('The maximum value is: ', max(int1,int2), '\n')
print('The minimum value is: ', min(int1, int2),'\n')

print('\n\nP2.6 page 81 Converting Meters to Miles, Feet and Inches')
print(100*0.000621371, ' miles in 100 meters\n')
print(100*3.28084, ' feet in 100 meters\n')
print(100*39.73, ' inches in 100 meters\n')