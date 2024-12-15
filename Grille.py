# -*- coding: utf-8 -*-
"""
Filename: Grille.py
Author: Evan
Date: 15 dec 2024
Description: Classe grille pour le jeu de la vie
"""

class Grille:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for x in range(self.dim)] for x in range(self.dim)] 

    def voisins_state(self, x, y):
        if x <= 0 or y <= 0 or x > self.dim or y > self.dim:
            print("Coordonnées > Dim")
            return 
        
        voisins_state = []
        
        top_left = voisins_state.append(self.grid[y-2][x-2]) if y-2 >= 0 and x-2 >= 0 else None
        top = voisins_state.append(self.grid[y-2][x-1]) if y-2 >= 0 else None
        top_right = voisins_state.append(self.grid[y-2][x]) if y-2 >= 0 and x < self.dim else None
        left = voisins_state.append(self.grid[y-1][x-2]) if x-2 >= 0 else None
        right = voisins_state.append(self.grid[y-1][x]) if x < self.dim else None
        bottom_left = voisins_state.append(self.grid[y][x-2]) if y < self.dim and x-2 >= 0 else None
        bottom = voisins_state.append(self.grid[y][x-1]) if y < self.dim else None
        bottom_right = voisins_state.append(self.grid[y][x]) if y < self.dim and x < self.dim else None

        count = voisins_state.count(1)

        return count
    
    def change_state(self, x, y):
        if x <= 0 or y <= 0 or x > self.dim or y > self.dim:
            print("Coordonnées > Dim")
            return
        
        count = self.voisins_state(x, y)
        cell = self.grid[y-1][x-1]

        if cell == 1:
            if count < 2 or count > 3:
                self.copy[y-1][x-1] = 0
            if count == 2 or count == 3:
                self.copy[y-1][x-1] = 1
        if cell == 0:
            if count == 3:
                self.copy[y-1][x-1] = 1
        
    def next_gen(self):
        self.copy = [[0 for x in range(self.dim)] for x in range(self.dim)] 
        for j in range(self.dim):
            for i in range(self.dim):
                self.change_state(i+1, j+1)
        self.grid = self.copy.copy()

    def flip_state(self, x, y):
        if x <= 0 or y <= 0 or x > self.dim or y > self.dim:
            print("Coordonnées > Dim")
            return
        
        self.grid[y-1][x-1] = 1 if self.grid[y-1][x-1] == 0 else 0

    def clear(self):
        self.grid = [[0 for x in range(self.dim)] for x in range(self.dim)]



        


        
            




        

        


