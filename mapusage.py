import math

def area(r):
    #Area of circle
    return(math.pi * (r**2))

radii = [2,5,7.1,0.3,10]

'''

areas = []

for r in radii:
    areais = area(r)
    print(areais)
    areas.append(areais)

print(areas)
'''

all_areas = list(map(area,radii))

print(all_areas)

    

