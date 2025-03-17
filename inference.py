import numpy as np

def update_probabilities(probabilities, x, y, color, direction, show_directions):
    likelihood = np.zeros_like(probabilities)
    for i in range(len(probabilities)):
        for j in range(len(probabilities[i])):
            d = abs(i - x) + abs(j - y)
            expected_distances = {
                "red": {0},
                "orange": {1, 2},
                "yellow": {3, 4},
                "lightgreen": {5, 6, 7, 8, 9, 10}
            }.get(color, set())

            if show_directions:
                likelihood[i, j] = 1 if d in expected_distances else 0
            else:
                likelihood[i, j] = 1 if d in expected_distances else 0

    probabilities *= likelihood
    probabilities /= np.sum(probabilities)
    return probabilities
