# -*- coding: utf-8 -*-
"""
Filename: Interface.py
Author: Evan
Date: 15 dec 2024
Description: Classe Interface pour le jeu de la vie
"""

import tkinter as tk

from Grille import Grille

class Interface:
    def __init__(self, root, dim=16):
        self.root = root
        self.root.title("Jeu de la vie")
        self.root.attributes("-fullscreen", True)
        self.canvas = tk.Canvas(self.root, width=800, height=800, bg="black")
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.pack()
        
        self.dim = dim
        self.speed = 5

        self.framerate = 1000 // self.speed

        self.grid = Grille(self.dim)

        self.cell_dim = (50 * 16) // self.dim

        self.draw_grid()

        self.button = tk.Button(self.root, text="Next", command=self.next_gen)
        self.button.pack()
        
        self.running = False
        self.update()

        self.playButton = tk.Button(self.root, text="Play", command=self.play)
        self.playButton.pack()

        self.clearButton = tk.Button(self.root, text="Clear", command=self.clear)
        self.clearButton.pack()

        self.dimLabel = tk.Label(self.root, text="Dimension de la grille : ")
        self.dimLabel.pack(side="left")
        self.dimEntry = tk.Entry(self.root)
        self.dimEntry.pack(side="left")
        self.dimButton = tk.Button(self.root, text="Valider", command=self.dim_up)
        self.dimButton.pack(side="left")

        self.speedUpButton = tk.Button(self.root, text="Speed Up", command=self.speed_up)
        self.speedUpButton.pack(side="right")

        self.speedDownButton = tk.Button(self.root, text="Speed Down", command=self.speed_down)
        self.speedDownButton.pack(side="right")

        self.speedLabel = tk.Label(self.root, text="Speed : " + str(self.speed))
        self.speedLabel.pack(side="right")

    def click(self, event):
        x = event.x // self.cell_dim 
        y = event.y // self.cell_dim
        self.grid.grid[y][x] = 1 if self.grid.grid[y][x] == 0 else 0
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_grid_state()
    
    def next_gen(self):
        self.grid.next_gen()
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_grid_state()
        
    def draw_grid(self):
        for i in range(0, 800, self.cell_dim):
            self.canvas.create_line(i, 0, i, 800, fill="grey")
            self.canvas.create_line(0, i, 800, i, fill="grey")
    
    def draw_cell(self, x, y):
        self.canvas.create_rectangle(x * self.cell_dim, y * self.cell_dim, x * self.cell_dim + self.cell_dim, y * self.cell_dim + self.cell_dim, fill="white")

    def draw_grid_state(self):
        for j in range(self.grid.dim):
            for i in range(self.grid.dim):
                if self.grid.grid[j][i] == 1:
                    self.draw_cell(i, j)

    def play(self):
        self.running = not self.running
        if self.running:
            self.playButton.config(text="Pause")
        else:
            self.playButton.config(text="Play")

    def update(self):
        if self.running:
            self.next_gen()
            self.root.after(self.framerate, self.update)
        else:
            self.root.after(500, self.update)

    def clear(self):
        self.canvas.delete("all")
        self.draw_grid()
        self.grid.clear()

    def dim_up(self):
        self.canvas.delete("all")
        self.dim = int(self.dimEntry.get())
        self.grid = Grille(self.dim)
        self.cell_dim = (50 * 16) // self.dim
        self.draw_grid()

    def speed_up(self):
        self.speed += 1
        self.framerate = 1000 // self.speed
        self.speedLabel.config(text="Speed : " + str(self.speed))

    def speed_down(self):
        if self.speed > 1:
            self.speed -= 1
            self.framerate = 1000 // self.speed
            self.speedLabel.config(text="Speed : " + str(self.speed))
        

            
            


