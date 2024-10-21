#we have x,y coordinates of following we need to find distance between nodes and store the result

# (1,2) (1,4) (4,6) (7,8)
import math
points = [(1, 2), (1, 4), (4, 6), (7, 8)]

def calculate_distances(points):
    distances = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        # Calculate the distance
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distances.append(distance)
    return distances
 
#distances between consecutive nodes
distances = calculate_distances(points)


for i in range(len(distances)):
    print(f"Distance between {points[i]} and {points[i+1]} is {distances[i]:.2f}")



# write a function that gives radial distance of this points theta of this point , angle of this point 
# write a function to move this function 
# 
