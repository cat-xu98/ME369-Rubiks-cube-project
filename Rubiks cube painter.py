#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 18:14:37 2020

@author: catherinexu, harrisonfrende
"""

from tkinter import *
from rubik_solver import utils

# ################################## Some global variables and constants ###############################################
width = 60  # width of a facelet in pixels
facelet_id = [[[0 for col in range(3)] for row in range(3)] for face in range(6)]
colorpick_id = [0 for i in range(6)]
curcol = None
t = ("U", "L", "F", "R", "B", "D")
cols = ("yellow", "green", "red", "blue", "orange", "white")
########################################################################################################################

################################################## Diverse functions ###################################################

def create_facelet_rects(a):
    """Initialize the facelet grid on the canvas."""
    offset = ((1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2))
    for f in range(6):
        for row in range(3):
            y = 10 + offset[f][1] * 3 * a + row * a
            for col in range(3):
                x = 10 + offset[f][0] * 3 * a + col * a
                facelet_id[f][row][col] = canvas.create_rectangle(x, y, x + a, y + a, fill="grey")
                if row == 1 and col == 1:
                    canvas.create_text(x + width // 2, y + width // 2, font=("", 14), text=t[f], state=DISABLED)
    for f in range(6):
        canvas.itemconfig(facelet_id[f][1][1], fill=cols[f])


def create_colorpick_rects(a):
    """Initialize the "paintbox" on the canvas."""
    global curcol
    global cols
    for i in range(6):
        x = (i % 3)*(a+5) + 7*a
        y = (i // 3)*(a+5) + 7*a
        colorpick_id[i] = canvas.create_rectangle(x, y, x + a, y + a, fill=cols[i])
        canvas.itemconfig(colorpick_id[0], width=4)
        curcol = cols[0]


def get_definition_string():
    """Generate the cube definition string from the facelet colors."""
    color_to_facelet = {}
    for i in range(6):
        color_to_facelet.update({canvas.itemcget(facelet_id[i][1][1], "fill"): t[i]})
    s = ''
    for f in range(6):
        for row in range(3):
            for col in range(3):
                s += color_to_facelet[canvas.itemcget(facelet_id[f][row][col], "fill")]
    return s

def click(event):
    """Define how to react on left mouse clicks."""
    global curcol
    idlist = canvas.find_withtag("current")
    if len(idlist) > 0:
        if idlist[0] in colorpick_id:
            curcol = canvas.itemcget("current", "fill")
            for i in range(6):
                canvas.itemconfig(colorpick_id[i], width=1)
            canvas.itemconfig("current", width=5)
        else:
            canvas.itemconfig("current", fill=curcol)
            
def done():
    string = ""
    for f in range(6):
        for row in range(3):
            for col in range(3):
                string += canvas.itemcget(facelet_id[f][row][col], "fill")[0]           
    solution = solve(string)
    return(print(solution))

def solve(cube_string):

    turns = utils.solve(cube_string, 'Kociemba') #list
    
    i = 1
    string = ""
    for m in turns:
        move = str(m)
        if "'" in move:
            direction = "counter-clockwise"
        else:
            direction = "clockwise"
            
        if '2' in move:
            num = "twice"
        else:
            num = "once"
            
        if "L" in move:
            face = "left"
        elif "F" in move:
            face = "front"
        elif "R" in move:
            face = "right"
        elif "B" in move:
            face = "back"
        elif "U" in move:
            face = "upper"
        elif "D" in move:
            face = "bottom"
        
        string += (str(i) + ") " + "Turn the " + face + " face " + num + " " + direction + "\n")
        i += 1
        
    return(print(string)) 
       
root = Tk()
root.wm_title("Rubik's Cube Painter")
canvas = Canvas(root, width=12 * width + 20, height=10 * width + 20)
canvas.pack()
canvas.bind("<Button-1>", click)

done = Button(root, text='Done', height=1, width=10, relief=RAISED, command=done)
done.pack()

create_facelet_rects(width)
create_colorpick_rects(width)
root.mainloop()
