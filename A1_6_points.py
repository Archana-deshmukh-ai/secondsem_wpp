import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

points = [(int(input("Enter x: ")), int(input("Enter y: ")), int(input("Enter z: "))) for _ in range(10)]

for i in range(3):
    ref_point = points[i]
    distances = [distance(ref_point, points[j]) for j in range(10) if j != i]
    nearest_index = distances.index(min(distances))
    print(f"The nearest neighbor to point {ref_point} is {points[nearest_index]}")
