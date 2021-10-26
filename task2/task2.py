from sys import argv

circle_file = argv[1]
dot_file = argv[2]

with open(f'{circle_file}','r') as file:
    mid = [float(i) for i in file.readline().strip().split(' ')]
    radius = float(file.readline())

with open (f'{dot_file}','r') as file:
    for line in file.readlines():
        dot = [float(i) for i in line.strip().split(' ')]
        if radius == ((dot[0]-mid[0])**2 + (dot[1]-mid[1])**2)**(0.5):
            print(0)
        elif (dot[0]-mid[0])**2 + (dot[1]-mid[1])**2 <= radius**2 and radius != ((dot[0]-mid[0])**2 + (dot[1]-mid[1])**2)**(0.5):
                print(1)
        else:
            print(2)
