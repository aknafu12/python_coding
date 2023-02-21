
import random as rd
planet = ['earth','jupyter','venus']

#appending
planet.append('mars')
#insert new 
planet.insert(1,'new value')
#delet second element
del planet[1]
print(planet)
#generate random number b/n 0 and 1 20 numbers 
for i in range(20):
    rand_0_1 = rd.random()
    # to make b/n 0 and 200 
    rand_0_200 = rd.random() 
    
    print('{:10.2f},{:>10.3f}'.format(rand_0_1,rand_0_200))

area_1 = float(input('enter first area:'))
area_2 = float(input('enter second area:'))
print('\tArea 1 \tArea 2')
print('{:>10.2f} {:>10.2f}'.format(area_1,area_2))
'''
for index in range (20):
    num1 = rd.random() #returns a random number between 0 and 1
    num2 = num1 * 200 #returns a random number between 0 and 20
    num3 = num1 * 200 + 50 #returns a random number between 50 and 25
    #print num1 to 4 decimal places,
    # #num2 to 2 decimal places, num3 to 1 decimal place
    # #each number occupies 20 spaces and is right aligned
    print("{:>20.4f}{:>20.2f}{:>20.1f}".format(num1,num2,num3))
'''
#Your code goes here
def  area_rectangle(length,breadth):  
    
    return length*breadth  

l = int(input('enter length of rectangle'))
b =int(input('enter breath of rectangle'))
area=area_rectangle(l,b)
print(area)

def myfunction(x1,x2,x3):
    return x1+x2+x3


arglist = [1,2,3,4,5,6,7,8,9]
for _ in range(3):
    print(myfunction(arglist[_+0],arglist[_+1],arglist[_+2]))
    # remove used arguments from the list 
    arglist= arglist[2:] 



























