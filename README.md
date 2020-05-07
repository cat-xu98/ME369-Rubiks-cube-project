# ME369-Rubiks-cube-project

## Packages Needed:
1. OpenCV
2. imutils
3. tkinter
4. rubik_solver

## Project Goal:

The end goal of this project is to combine existing packages with custom code into a script that outputs solution steps to solve a scrambled rubik's cube. The inputs will come as two images, each of opposite verticies of a rubik's cube such that all six faces are visible when the two images are stiched together. Computer vision would then be employed to determine the color of each cublet in a logical order. This logical order is top to bottom - left to right for each face in the face order of top, left, front, right, back, bottom. These cublet colors would then be passed to a rubik's cube solver package (why reinvent the wheel) that outputs the solution steps based on the current scrambled cube. Finally, the custom code would reformat the solution steps in a way that is easily understood, perhaps even including an animation of the users cube being solved step by step.
  
## General Methodology:

### Achieved Functionality:
1. Create tkinter UI with "unfolded" cube that has face position and color lables
2. UI allows user to color in each non-center cubelt with a six-color palet (white, yellow, red, organge, blue, green)
3. Backend code records values of user inputs into a "scramble string"
4. Scramble string is passed to rubik_solver package to determine solutions steps
5. Back end code reformats outut of rubik_solver and prints easily understood directions to console

### In the Works Functionality:
1. Create black and white mask to simplify image of rubik's cube face
2. Use HSV color ranges for each possible color (white, yellow, red, organge, blue, green) to determine color each cubelet
3. Filter out contours that are too small or too large
4. Check color value at centroid of each cublet contour
5. Save color of cubelets in top to bottom - left to right order in a "scramble string"
6. Pass scramble string to rubik_solver package to determine solutions steps
7. Back end code reformats outut of rubik_solver and prints easily understood directions to console

### Reach Functionality:
1. Create black and white mask to simplify image of rubik's cube faces
2. Train computer vision algorithm with sample images to improve countour recognition
3. Backend code determines HSV value at centroid of each contour
4. Save color of cubelets in top to bottom - left to right order in a "scramble string"
5. Pass scramble string to rubik_solver package to determine solutions steps
6. Back end code reformats outut of rubik_solver and prints easily understood directions to console

## Achieved Functionality Code Sources:

### Steps 1-3:
Code acquired from [RubiksCube-TwophaseSover](https://github.com/hkociemba/RubiksCube-TwophaseSolver)\
License: GNU General Public License v3.0\
Changes Made:
1. Removed local and/or remote server capability
2. Removed functions to change facelet colors
3. Added function to store facelet color information in a string and print said string
4. Removed solve button from interface (was dependent on local and/or remote server capability)

### Step 4:
Code acquired from [rubik-solver](https://pypi.org/project/rubik-solver/)\
License: MIT\
Changes Made:
1. None

This package was called with the input being the string made in the previous step.

### Step 5:
Code made by team.\
This section of code takes the outout of the rubik-solver package and formats it in an easy to read way instead of the shorthand used in rubik's cube algorithms. For example, a F' in shorthand means move the front face counterclockwise. This section of code writes that out in plain english.

## In the Works Functionality Code Sources:

### Steps 1 and 2:
Code aquired from [stack overflow question answer by nathancy](https://stackoverflow.com/questions/24916870/python-opencv-rubiks-cube-solver-color-extraction/58018944#58018944)\
Changes Made:
1. Added color ranges for green, red, and white
2. Added functionality seen in steps 3 and 4

### Steps 3 and 4:
Code acquired from [stack overflow question answer by Abid Rhaman K](https://stackoverflow.com/questions/14476683/identifying-color-sequence-in-opencv)\
Changes Made:
1. Only used the contour size filter and color range recognition at the centroid of each identified countour

### Implementation of steps 5-7:
Adding these steps will be much like steps 4 and 5 of the functional code. The main hangup on this version of the project is getting openCV to recognize every facelets in an image and assigning the correct color to each identified facelet. This comes down to finding the proper lighting to take the picture in the first place and the correct HSV value ranges for each of the six possible colors.
