import random

GRID_ROWS = 8
GRID_COLS = 13

def place_phantom():
    return random.randint(0, GRID_ROWS - 1), random.randint(0, GRID_COLS - 1)

def initialize_prior_probabilities():
    return [[1 / (GRID_ROWS * GRID_COLS) for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def sense_distance(distance):
    if distance == 0:
        return "red"
    elif distance <= 2:
        return "orange"
    elif distance <= 4:
        return "yellow"
    else:
        return "lightgreen"

def calculate_direction(player_x, player_y, phantom_x, phantom_y):
    if player_x < phantom_x and player_y < phantom_y:
        return "SE"
    elif player_x < phantom_x and player_y > phantom_y:
        return "SW"
    elif player_x > phantom_x and player_y < phantom_y:
        return "NE"
    elif player_x > phantom_x and player_y > phantom_y:
        return "NW"
    elif player_x < phantom_x:
        return "S"
    elif player_x > phantom_x:
        return "N"
    elif player_y < phantom_y:
        return "E"
    elif player_y > phantom_y:
        return "W"
    else:
        return "HERE"
