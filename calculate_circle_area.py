import math

def calculate_circle_area(radius):
    return (radius ** 2) * math.pi

data = int(input("Enter radius of circle: "))
area = calculate_circle_area(data)
print(area)
