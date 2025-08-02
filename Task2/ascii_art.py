class draw:
    def draw_hollow_circle(radius, width, scale):
        
        for y in range(-radius+1, radius):
            for x in range(-radius+1, radius):

                edge = ((x*x + y*y)/radius - radius)+scale

                if edge > -width and edge < 1:
                    print(".", end="")
                else:
                    print("#", end="")
            print()

if __name__ == "__main__":
    draw.draw_hollow_circle(20,5,5)