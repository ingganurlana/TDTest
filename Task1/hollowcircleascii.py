radius = 20
width = 5
scale = 5

for y in range(-radius+1, radius):
    for x in range(-radius+1, radius):

        edge = ((x*x + y*y)/radius - radius)+scale

        if edge > -width and edge < 1:
            print(".", end="")
        else:
            print("#", end="")
    print()