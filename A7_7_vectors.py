'''7. Create a class for representing any 2-D point or vector. The methods inside this class include 
its magnitude and its rotation with respect to the X-axis. Using the objects define functions for 
calculating the distance between two vectors, dot product, cross product of two vectors. Extend 
the 2-D vectors into 3-D using the concept of inheritance. Update the methods according to 3-
D.'''
import math
import sys
class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
       
    def __sub__(self,other):
        return self-other
    def __add__(self,other):
        return self+other
    def __multi__(self,other):
        return self*other
    def __div__(self,other):
        if(other==0):
            return 
        else:
            return self/other
    def __eq__(self,other):
        return self==other
    
    def magnitude(self):
        return math.sqrt((self.x**2)+(self.y**2))
    
    def Angle(self):
        angle=math.arctan(self.y/self.x)
        return angle
    
    def Rotation(self):
        result=vector()
        result.x=self.x*math.cosine(self.Angle())-self.y*math.sine(self.Angle())
        result.y=self.x*math.sine(self.Angle())+self.y*math.cosine(self.Angle())
        print(result.x,"+",result.y)
    
    def distance(self,other):
        return math.sqrt((self.y-other.y)**2+(self.x-other.x)**2) 
    
    def dot_product(self,other):
        print(self.x*other.x+self.y*other.y)
    
    def crossproduct(self,other):
        print(self.x*other.y-self.y*other.x)
    
class ThreeD_vectors(vector):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

    def magnitude(self):
        return math.sqrt((self.x**2+self.y**2+self.z**2))
    
    def Angle(self):
        angle=math.arctan(self.y/self.x)
        return angle
    
    def rotate(self):
        result=ThreeD_vectors()
        result.x=self.x
        result.y=self.y*math.cosine(self.Angle)-self.z*math.sine(self.Angle)
        result.z=self.y*math.sine(self.Angle)+self.z*math.cosine(self.Angle)
        print(result.x,"+",result.y,"+",result.z)

    def distance(self,other):
        return math.sqrt((self.y-other.y)**2+(self.x-other.x)**2+(self.z-other.z)**2) 
    
    def dot_product(self,other):
        print(self.x*other.x+self.y*other.y+self.z*other.z)
    
    def cross_product(self,other):
        result=ThreeD_vectors()
        result.x=self.y*other.z-self.z*other.y
        result.y=self.z*other.x-self.x*other.z
        result.z=self.x*other.y-self.y*other.x
        print(result.magnitude(self))


print("Welcome to the vectors!!")
num=int(input("Enter 2 for 2d,3 for 3d and -1 for exit: "))
while True:
    if(num==2):
        twod=vector()
        twod.x=int(input("Enter the value of x: "))
        twod.y=int(input("Enter the value of y: "))
        while True:
            print("\nEnter 1.Magnitude\n2.Angle\n3.rotation\n4.distance\n5.dot product\n6.cross product ")
            choice=int(input())

            if choice==1:
                magnitude=twod.magnitude()
                print(f"\nThe magnitude of the vector is {magnitude}")

            elif choice==2:
                angle=twod.Angle()
                print(f"\nThe angle of the given vector is {angle}")

            elif choice==3:
                rotation=twod.rotate()
            
            elif choice==4:
                other=vector()
                other.x=int(input("Enter the value of x: "))
                other.y=int(input("Enter the value of y: "))
                distance=twod.distance(other)
                print(f"The distance is {distance}")

            elif choice==5:
                other=vector()
                other.x=int(input("Enter the value of x: "))
                other.y=int(input("Enter the value of y: "))
                twod.dot_product(other)

            elif choice==6:
                other=vector()
                other.x=int(input("Enter the value of x: "))
                other.y=int(input("Enter the value of y: "))
                twod.cross_product(other)

            else:
                print("Bye Bye")
                sys.exit(0)

    elif(num==3):
        threed=ThreeD_vectors()
        threed.x=int(input("Enter the value of x: "))
        threed.y=int(input("Enter the value of y: "))
        threed.z=int(input("Enter the value of z: "))
        while True:
            print("\nEnter 1.Magnitude\n2.Angle\n3.rotation\n4.distance\n5.dot product\n6.cross product\n7.exit ")
            choice=int(input())

            if choice==1:
                magnitude=threed.magnitude()
                print(f"\nThe magnitude of the vector is {magnitude}")

            elif choice==2:
                angle=threed.Angle()
                print(f"\nThe angle of the given vector is {angle}")

            elif choice==3:
                rotation=threed.rotate()
                
            elif choice==4:
                other=vector()
                other.x=int(input("Enter the value of x: "))
                other.y=int(input("Enter the value of y: "))
                other.z=int(input("Enter the value of z: "))
                distance=threed.distance(other)
                print(f"The distance is {distance}")

            elif choice==5:
                other=vector()
                other.x=int(input("Enter the value of x: "))
                other.y=int(input("Enter the value of y: "))
                other.z=int(input("Enter the value of z: "))
                threed.dot_product(other)
                
            elif choice==6:
                other=vector()
                other.x=int(input("Enter the value of x: "))
                other.y=int(input("Enter the value of y: "))
                other.z=int(input("Enter the value of z: "))
                threed.cross_product(other)

            else:   
                print("bye bye")
                sys.exit(0)
    elif num==-1:
        print("Bye Bye")
        sys.exit(0)
        
    else :
        print("INVALID!!  Please try again")







                
                


            

            

            

            
                
            
            




                
                


            

            

            

            
                
            
            