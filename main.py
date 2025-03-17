"""
Find the Phantom Game
Developed by Maria Chmite, Salim El Ghersse, and Mohamed Ouballouk.
"""

import tkinter as tk
from gui import PhantomHunterGame

if __name__ == "__main__":
    root = tk.Tk()
    game = PhantomHunterGame(root)
    root.mainloop()
