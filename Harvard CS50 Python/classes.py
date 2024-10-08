# template for a type of object = class
# define a new class and then after defining
#  "point" you can create other "point(s)"

# we need some way to say that when I create a point what should happen
# to create a class you use magic method __init__
# __init__ is a method/function that is called every time we want to reuse the class/ in this case
# create a new point

# All functions on objects themselves aka methods take the first argument of "self". It represents 
# the object in question. It references the object you are currently dealing with it.

# store data inside of point with self; point needs an x and y value so to create one 
# we provide those values
# to store all of this data inside of Point. recall self is representing Point itself. Allow 
# Point to have its own x and y data but assigning it to the point using dot notation. (ex:self.x)
# input1 and input2 can be called anything. The important thing is the two 
# input values are being stored in the in point itself represented by properties x and y

class Point():
    def __init__(self,input1,input2):
        self.x = input1
        self.y = input2
# to create a new point called p. provide input 1 and 2       
p = Point(2,8)
# I can print out info about the point now. Using dot notation to say go 
# into the point access the x and y value of that point
print(p.x)
print(p.y)

# We have a function called init that creates a point by storing the inputs inside the object in
# a property called x and one called y. So that later I can create a point 
# that calls the init function and access the data inside .