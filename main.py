# -*- coding: utf-8 -*-
"""
File: main.py
Author: Evan
Date: 
Ce fichier contient le code principal pour lancer le jeu.
"""

import tkinter as tk
from Interface import Interface

def main():
    """
    Fonction principale pour lancer le menu du jeu de morpion.
    """
    root = tk.Tk()
    game = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()