# Assignment 3 : You first Python Program

# How much building materials are needed to cover the entire floor as well as how much baseboard we should have that will be installed into the room
# Imagine that you would like to remodel one of your rooms in your house/home/apparent. Select any room of your choice and measure it. Have all the measurements ready and use them as input parameters to your Python program.

FloorWidth = float(input('Please input Width Of The Room: '))
FloorLength = float(input('Please input Length Of The Room: '))

RoomArea = FloorWidth * FloorLength

print(f'Room Area Need To Be Covered: ', RoomArea )

RoomPerimeter = ( FloorWidth + FloorWidth ) * 2

print(f'Room Perimeter Need To Be Installed Base Board : ', RoomPerimeter )