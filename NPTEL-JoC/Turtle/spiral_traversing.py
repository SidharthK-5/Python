"""
Spiral traversing with turtle graphics
"""

import turtle
turtle.bgcolor("black")
seurat = turtle.Turtle()

width = 5
height = 7
dot_distance = 25
seurat.setpos(-250, 250)

def spiral(total_rows, total_cols):
    row_iter = 0
    col_iter = 0
    seurat.color("white")
    seurat.pensize(3)
    
    while row_iter < total_rows and col_iter < total_cols:
        seurat.penup()
        for _ in range(col_iter, total_cols):
            seurat.forward(dot_distance)
            seurat.dot()
        row_iter += 1
        seurat.right(90)
        
        for _ in range(row_iter, total_rows):
            seurat.forward(dot_distance)
            seurat.dot()
        total_cols -= 1
        seurat.right(90)
        
        if row_iter < total_rows:
            for _ in range(total_cols-1, col_iter-1, -1):
                seurat.forward(dot_distance)
                seurat.dot()
            total_rows -= 1
            seurat.right(90)
            
        if col_iter < total_cols:
            for _ in range(total_rows-1, row_iter-1, -1):
                seurat.forward(dot_distance)
                seurat.dot()
            col_iter += 1
            seurat.right(90)
            
spiral(width, height)
turtle.done()
