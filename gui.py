import tkinter as tk
import numpy as np
from tkinter import messagebox
from sensors import place_phantom, initialize_prior_probabilities, calculate_distance, sense_distance, calculate_direction
from inference import update_probabilities

# Game settings
GRID_ROWS = 8
GRID_COLS = 13
STARTING_POINTS = 10
STARTING_ATTEMPTS = 2
STARTING_PHANTOMS = 1

class PhantomHunterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Find the Phantom")
        self.root.configure(bg="gray")
        self.phantom_x, self.phantom_y = place_phantom()
        self.remaining_points = STARTING_POINTS
        self.remaining_attempts = STARTING_ATTEMPTS
        self.phantoms_left = STARTING_PHANTOMS
        self.bust_mode = False
        self.display_probabilities = False
        self.show_directions = False
        self.probabilities = initialize_prior_probabilities()
        self.grid_buttons = []
        self.setup_gui()

    def setup_gui(self):
        # Configure the grid
        for i in range(GRID_ROWS):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(GRID_COLS):
            self.root.grid_columnconfigure(j, weight=1)

        # Create grid buttons
        for i in range(GRID_ROWS):
            row = []
            for j in range(GRID_COLS):
                btn = tk.Button(self.root, text="", bg="lightgray", fg="black",
                                font=("Helvetica", 15), command=lambda x=i, y=j: self.handle_click(x, y))
                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
                row.append(btn)
            self.grid_buttons.append(row)

        # Side panel
        self.status_label = tk.Label(self.root, text=f"PHANTOMS: {self.phantoms_left}\nATTEMPTS LEFT: {self.remaining_attempts}\nPOINTS: {self.remaining_points}",
                                     bg="gray", fg="black", font=("Helvetica", 12), justify="left")
        self.status_label.grid(row=0, column=GRID_COLS + 2, rowspan=2, columnspan=3, sticky="nw", padx=10, pady=10)

        self.bust_button = tk.Button(self.root, text="GUESS", bg="lightgray", fg="black",
                                     font=("Helvetica", 12), command=self.toggle_bust_mode)
        self.bust_button.grid(row=2, column=GRID_COLS, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.probabilities_button = tk.Button(self.root, text="SHOW CHANCES", bg="lightgray", fg="black",
                                              font=("Helvetica", 12), command=self.toggle_probability_display)
        self.probabilities_button.grid(row=3, column=GRID_COLS, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.reset_button = tk.Button(self.root, text="START OVER", bg="lightgray", fg="black",
                                      font=("Helvetica", 12), command=self.reset_game)
        self.reset_button.grid(row=5, column=GRID_COLS, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.direction_button = tk.Button(self.root, text="SHOW DIRECTION", bg="lightgray", fg="black",
                                          font=("Helvetica", 12), command=self.toggle_direction_mode)
        self.direction_button.grid(row=4, column=GRID_COLS, columnspan=3, sticky="nsew", padx=10, pady=10)

        self.message_label = tk.Label(self.root, text="MESSAGES:", bg="gray", fg="black", font=("Helvetica", 10))
        self.message_label.grid(row=6, column=GRID_COLS, rowspan=2, columnspan=3, sticky="nw", padx=10, pady=10)

    def toggle_direction_mode(self):
        self.show_directions = not self.show_directions
        self.direction_button.config(text="HIDE DIRECTION" if self.show_directions else "SHOW DIRECTION")

    def toggle_probability_display(self):
        self.display_probabilities = not self.display_probabilities
        for i in range(GRID_ROWS):
            for j in range(GRID_COLS):
                if self.display_probabilities and self.probabilities[i][j] > 0:
                    self.grid_buttons[i][j].config(text=f"{self.probabilities[i][j]:.2f}")
                else:
                    self.grid_buttons[i][j].config(text="")
        self.probabilities_button.config(text="HIDE CHANCES" if self.display_probabilities else "SHOW CHANCES")

    def handle_click(self, x, y):
        if self.bust_mode:
            self.guess_phantom(x, y)
        else:
            if self.remaining_points > 0:
                distance = calculate_distance(x, y, self.phantom_x, self.phantom_y)
                color = sense_distance(distance)
                direction = ""
                if self.show_directions:
                    direction = calculate_direction(x, y, self.phantom_x, self.phantom_y)
                    self.message_label.config(text=f"Direction: {direction}")
                self.probabilities = update_probabilities(self.probabilities, x, y, color, direction, self.show_directions)
                self.remaining_points -= 1
                self.update_status()

                if self.display_probabilities:
                    self.toggle_probability_display()
                    self.toggle_probability_display()

                self.grid_buttons[x][y].config(text=f"{direction}", bg=color)

                if distance == 0:
                    self.message_label.config(text="Game Over! You clicked on the phantom without guessing!")
                    return
            else:
                self.message_label.config(text="Out of points!")

    def toggle_bust_mode(self):
        self.bust_mode = not self.bust_mode
        if self.remaining_attempts > 0 and self.bust_mode:
            self.message_label.config(text="Guess mode activated! Choose wisely.")
        elif self.remaining_attempts <= 0:
            self.message_label.config(text="No guesses left!")
        else:
            self.bust_mode = False
            self.message_label.config(text="Guess mode deactivated.")

    def guess_phantom(self, x, y):
        if (x, y) == (self.phantom_x, self.phantom_y):
            self.grid_buttons[x][y].config(text="HERE", bg="red")
            self.message_label.config(text="You win! Phantom caught!")
            self.bust_mode = False
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts <= 0:
                self.message_label.config(text="Game Over! No guesses left.")
            else:
                self.message_label.config(text="Wrong guess! Try again.")
        self.update_status()

    def reset_game(self):
        self.phantom_x, self.phantom_y = place_phantom()
        self.remaining_points = STARTING_POINTS
        self.remaining_attempts = STARTING_ATTEMPTS
        self.bust_mode = False
        self.probabilities = initialize_prior_probabilities()
        for i in range(GRID_ROWS):
            for j in range(GRID_COLS):
                self.grid_buttons[i][j].config(text=f"{self.probabilities[i][j]:.2f}" if self.display_probabilities else "", bg="lightgray")
        self.update_status()
        self.message_label.config(text="Game restarted! Good luck!")

    def update_status(self):
        self.status_label.config(text=f"PHANTOMS: 1\nATTEMPTS LEFT: {self.remaining_attempts}\nPOINTS: {self.remaining_points}")
