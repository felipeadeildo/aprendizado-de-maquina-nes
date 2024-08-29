from string import ascii_lowercase
from typing import List, Tuple, Union

from perceptron import Perceptron
from utils import (
    Color,
    evaluate_target_function,
    generate_data,
    generate_target_function,
)

INSTRUCTIONS = (
    f"{Color.text('8. Qual das seguintes opções está mais próxima de P[f(x) ≠ g(x)] para N = 10?', Color.BRIGHT_CYAN)}\n"
    f"{Color.text('[a] 0.001', Color.BRIGHT_RED)}\n"
    f"{Color.text('[b] 0.01', Color.BRIGHT_RED)}\n"
    f"{Color.text('[c] 0.1', Color.BRIGHT_RED)}\n"
    f"{Color.text('[d] 0.5', Color.BRIGHT_RED)}"
)


def simulate_run(n_points: int, n_test_points: int = 1000) -> Tuple[int, float]:
    """Simula uma execução do Perceptron Learning Algorithm.

    Args:
        n_points (int): Número de pontos de treinamento.
        n_test_points (int): Número de pontos de teste para estimar P[f(x) ≠ g(x)].

    Returns:
        Tuple[int, float]: Número de iterações para convergência e a estimativa de P[f(x) ≠ g(x)].
    """
    point1, point2 = generate_target_function()

    X_train, y_train = generate_data(n_points)
    y_train: List[Union[int, float]] = [
        evaluate_target_function(point1, point2, x) for x in X_train
    ]

    pla = Perceptron(n_iters=1000)
    pla.fit(X_train, y_train)

    X_test, _ = generate_data(n_test_points)
    y_test_f = [evaluate_target_function(point1, point2, x) for x in X_test]
    y_test_g = [pla.predict([1] + x) for x in X_test]

    # Calcula P[f(x) ≠ g(x)]
    disagreement = sum(1 if f != g else 0 for f, g in zip(y_test_f, y_test_g)) / len(
        y_test_f
    )

    return pla.iterations, disagreement


def run() -> None:
    """Roda a simulação 1000 vezes e calcula as médias de iterações e P[f(x) ≠ g(x)]."""
    total_iterations = 0
    total_disagreement = 0
    n_runs = 1000
    n_points = 10

    for i in range(n_runs):
        print(
            Color.text(f"Simulação {i + 1} de {n_runs}...", Color.BRIGHT_YELLOW),
            end="\r",
            flush=True,
        )
        iterations, disagreement = simulate_run(n_points)
        total_iterations += iterations
        total_disagreement += disagreement

    average_iterations = total_iterations / n_runs
    average_disagreement = total_disagreement / n_runs

    print(
        Color.text(
            f"\nMédia de iterações para convergência com N = {n_points}: {average_iterations:.3f}",
            Color.BRIGHT_CYAN,
        )
    )
    print(
        Color.text(
            f"Média de P[f(x) ≠ g(x)] para N = {n_points}: {average_disagreement:.3f}",
            Color.BRIGHT_CYAN,
        )
    )

    alternatives_disagreement = zip(ascii_lowercase, [0.001, 0.01, 0.1, 0.5])
    closest_disagreement = min(
        alternatives_disagreement, key=lambda x: abs(x[1] - average_disagreement)
    )
    print(
        Color.text(
            f"Alternativa mais próxima para P[f(x) ≠ g(x)]: {closest_disagreement[0]}) {closest_disagreement[1]}",
            Color.GREEN,
        )
    )


if __name__ == "__main__":
    run()
