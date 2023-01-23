import random
cars =["Bugati","Mercedes","Hyundai"]
cars.append('Tesla')
cars.append('BMW')
cars.remove('Hyundai')
random.shuffle(cars)

print(cars)
