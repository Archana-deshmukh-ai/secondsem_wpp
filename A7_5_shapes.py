class shapes:

    def area(self):
        pass

    def perimeter(self):
        pass
    

class square(shapes):

    def area(self,length):
        area=(length**2)
        return area
    
    def perimeter(self,length):
        perimeter=(length*4)
        return perimeter
    

class rectangle(shapes):
    def area(self,length,breadth):
        area=(length*breadth)
        return area
    
    def perimeter(self,length,breadth):
        perimeter=2*(length+breadth)
        return perimeter
    


print("Welcome to shapes")
shape=input("Now,enter your shape: ")

if(shape=='square'):
    
    length=float(input("enter the length of your square: "))
    shape=square()
    area=shape.area(length)
    perimeter=shape.perimeter(length)
    print(f"\nThe area and perimeter of the given square is {area} and {perimeter} ")

elif(shape=='rectangle'):
    
    length=float(input("enter the length of your rectangle: "))
    breadth=float(input("enter the breadth of your rectangle: "))
    shape=rectangle()
    area=shape.area(length,breadth)
    perimeter=shape.perimeter(length,breadth)
    print(f"\nThe area and perimeter of the given square is {area} and {perimeter}")

