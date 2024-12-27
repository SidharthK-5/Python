"""
Program to print the elements of a matrix in a spiral order with different colours
"""

import turtle
import random

turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 5
height = 7
dot_distance = 25
seurat.penup()
seurat.setpos(-250, 250)

list_of_colours = ["white", "yellow", "blue", "green", "red", "orange", "purple", "pink", "violet", "cyan", "magenta", "brown", "gray"]

def spiral_print(rows, cols):
    row_iter = 0
    col_iter = 0
    f = 0
    
    seurat.color(random.choice(list_of_colours))
    seurat.pensize(3)
    
    while row_iter < rows and col_iter < cols:
        # Print the first row from the remaining rows
        if f == 1:
            seurat.right(90)
            
        for _ in range(col_iter, cols):
            seurat.dot()
            seurat.forward(dot_distance)
            seurat.dot()
        row_iter += 1
        f = 1
        
        # Print the last column from the remaining columns
        seurat.right(90)
        seurat.color(random.choice(list_of_colours))
        
        for _ in range(row_iter, rows):
            seurat.dot()
            seurat.forward(dot_distance)
            
        cols -= 1
        
        # Print the last row from the remaining rows
        seurat.right(90)
        seurat.color(random.choice(list_of_colours))
        
        if row_iter < rows:
            for _ in range(cols-1, col_iter-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
            rows -= 1
            
        # Print the first column from the remaining columns
        seurat.right(90)
        seurat.color(random.choice(list_of_colours))
        
        if col_iter < cols:
            for _ in range(rows-1, row_iter-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
            col_iter += 1
     
if __name__ == "__main__":    
    spiral_print(width, height)
    turtle.done()