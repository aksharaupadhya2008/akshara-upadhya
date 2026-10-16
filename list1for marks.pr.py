import math 
r=float(input("enter the radius of the circle:"))
area=math.pi*r**2
circumference=2*math.pi*r
area_integer=int(area)
print(f"area :{area:2f}")
print(f"circumference:{circumference:2f}")
print(f"area_integer:{area_integer}")
