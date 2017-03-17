# MPsense.py

from sense_hat import SenseHat

# Set up grid

def printgrid():
    sense.clear()
    for y in range(0,3):
        output = ""
        for x in range(0,3):
		if twodarray[x][y] == "X":
			sense.set_pixel(x,y,0,225,0)
		elif twodarray[x][y] == "O":
			sense.set_pixel(x,y,225,0,0)
		output = output + str(twodarray[x][y])
        print(output)
  
sense = SenseHat()

# Set up 2D Array

    # E.g. 1D Array
    # onedarray = []

twodarray = [[0 for x in range(0,3)] for y in range(0,3)]

# Display 2D Array

printgrid()

# Change 2D Array

xpos = int(input("Please enter horizontal position (0)"))
ypos = int(input("Please enter vertical position (0)"))
twodarray[xpos][ypos] = "X"

# Display 2D Array

printgrid()

# Change 2D Array

twodarray[1][0] = "O"

# Display 2D Array

printgrid()

# Change 2D Array

xpos = int(input("Please enter horizontal position (0)"))
ypos = int(input("Please enter vertical position (1)"))
twodarray[xpos][ypos] = "X"

# Display 2D Array

printgrid()

# Change 2D Array

twodarray[0][2] = "O"

# Display 2D Array

printgrid()

# Change 2D Array

xpos = int(input("Please enter horizontal position (1)"))
ypos = int(input("Please enter vertical position (1)"))
twodarray[xpos][ypos] = "X"

# Display 2D Array

printgrid()

# Change 2D Array

twodarray[2][2] = "O"

# Display 2D Array

printgrid()

# Change 2D Array

xpos = int(input("Please enter horizontal position (2)"))
ypos = int(input("Please enter vertical position (0)"))
twodarray[xpos][ypos] = "X"

# Display 2D Array

printgrid()

# Change 2D Array

twodarray[2][1] = "O"

# Display 2D Array

printgrid()

sense.show_message("HEHEHE LOL")
