# In order to get a reliable estimate for these two quantities, you should repeat the
# experiment for 1000 runs (each run as specified above) and take the average over
# these runs.

# 7. Take N = 10. How many iterations does it take on average for the PLA to converge
# for N = 10 training points? Pick the value closes to your results.
# (again, 'closest' means: |your answer - given option| is closest to 0).

import random
from typing import List, Union

from perceptron import Perceptron


def generate_data(n_points: int = 10):
    """Gera os dados de treinamento e a função alvo."""
    X = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(n_points)]
    point1 = [random.uniform(-1, 1) for _ in range(2)]
    point2 = [random.uniform(-1, 1) for _ in range(2)]

    def target_function(x):
        """Calcula a função alvo baseada na linha."""
        return (
            1
            if (x[1] - point1[1]) * (point2[0] - point1[0])
            > (point2[1] - point1[1]) * (x[0] - point1[0])
            else 0
        )

    y: List[Union[float, int]] = [target_function(x) for x in X]
    return X, y


def run():
    n_runs = 1000
    total_iterations = 0
    n_points = 10

    for _ in range(n_runs):
        X, y = generate_data(n_points)
        pla = Perceptron()
        pla.fit(X, y)
        total_iterations += pla.iterations

    average_iterations = total_iterations / n_runs

    print(
        f"Média de iterações para convergência com N = {n_points}: {average_iterations}"
    )
