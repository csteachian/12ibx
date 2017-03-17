# 2D Array
# By Mr Simpson
# 17th March 2017

from sense_hat import SenseHat

sense = SenseHat()

def printgrid():
    for y in range(0,3):
        output = ""
        for x in range(0,3):
	    if twodarray[x][y] == "X":
	        sense.set_pixel(x,y,0,255,0)
	    elif twodarray[x][y] == "O":
	        sense.set_pixel(x,y,255,0,0)
            output = output + str(twodarray[x][y])
        print(output)
    print()

# Set up a 2D array
twodarray = [[0 for x in range(0,3)]for y in range(0,3)]
# Display 2D array
printgrid()
# Change 2D array
xpos = int(input("Please enter horizontal position (0,2)"))
ypos = int(input("Please enter vertical position (0,2)"))
twodarray[xpos][ypos] = "X"
# Display 2D array
printgrid()
# Change 2D array
twodarray[1][0] = "O"
# Display 2D array
printgrid()

#sense.show_message("hi from mr simpson")
