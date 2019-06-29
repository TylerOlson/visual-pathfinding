from grid import Grid
import tkinter as tk
import sys

HEIGHT = 600
WIDTH = 800

sys.setrecursionlimit(10000)
root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="white")
main_grid = Grid(15, 80, root, canvas, WIDTH, HEIGHT)


def flood():
    main_grid.flood(0, 0, "white", "green")


decrease_scale_button = tk.Button(root, text="Decrease Grid Scale", command=main_grid.decrease_scale)
increase_scale_button = tk.Button(root, text="Increase Grid Scale", command=main_grid.increase_scale)
clear_array_button = tk.Button(root, text="Clear Array", command=main_grid.clear_array)
flood_button = tk.Button(root, text="Flood", command=flood)


def drawing(event):
    grid_x = int(event.x / main_grid.scale)
    grid_y = int(event.y / main_grid.scale)
    fill_color = ""
    if (event.state == 256):
        fill_color = "red"
    elif (event.state == 1024):
        fill_color = "blue"
    main_grid.change_color(grid_x, grid_y, fill_color)


canvas.bind("<B1-Motion>", drawing)
canvas.bind("<B3-Motion>", drawing)
canvas.pack()
decrease_scale_button.pack()
increase_scale_button.pack()
clear_array_button.pack()
flood_button.pack()
root.mainloop()
