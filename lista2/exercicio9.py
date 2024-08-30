from typing import List

from linear_regression import LinearRegression
from utils import Color, generate_data_with_noise, sign, transform_features

INSTRUCTIONS = (
    f"{Color.text('Agora, transforme os N = 1000 dados de treinamento no seguinte vetor de características não lineares:', Color.BRIGHT_CYAN)}\n"
    f"{Color.text('(1, x1, x2, x1x2, x1^2, x2^2)', Color.BRIGHT_RED)}\n\n"
    f"{Color.text('9. Encontre o vetor de pesos w que corresponde à solução da Regressão Linear. ', Color.BRIGHT_BLUE)}"
    f"{Color.text('Qual das seguintes hipóteses está mais próxima da que você encontrou?', Color.BRIGHT_BLUE)}\n"
    f"{Color.text('Mais próxima significa aquela que mais concorda com sua hipótese (tem a maior probabilidade de concordar em um ponto selecionado aleatoriamente).', Color.BRIGHT_PURPLE)}\n"
    f"{Color.text('Escolha a opção mais próxima do seu resultado:', Color.BRIGHT_PURPLE)}\n"
    f"{Color.text('[a] g(x1, x2) = sign(−1 − 0.05x1 + 0.08x2 + 0.13x1x2 + 1.5x1^2 + 1.5x2^2)', Color.TEAL)}\n"
    f"{Color.text('[b] g(x1, x2) = sign(−1 − 0.05x1 + 0.08x2 + 0.13x1x2 + 1.5x1^2 + 15x2^2)', Color.TEAL)}\n"
    f"{Color.text('[c] g(x1, x2) = sign(−1 − 0.05x1 + 0.08x2 + 0.13x1x2 + 15x1^2 + 1.5x2^2)', Color.TEAL)}\n"
    f"{Color.text('[d] g(x1, x2) = sign(−1 − 1.5x1 + 0.08x2 + 0.13x1x2 + 0.05x1^2 + 0.05x2^2)', Color.TEAL)}\n"
    f"{Color.text('[e] g(x1, x2) = sign(−1 − 0.05x1 + 0.08x2 + 1.5x1x2 + 0.15x1^2 + 0.15x2^2)', Color.TEAL)}"
)

HYPOTHESES = {
    "a": [-1, -0.05, 0.08, 0.13, 1.5, 1.5],
    "b": [-1, -0.05, 0.08, 0.13, 1.5, 15],
    "c": [-1, -0.05, 0.08, 0.13, 15, 1.5],
    "d": [-1, -1.5, 0.08, 0.13, 0.05, 0.05],
    "e": [-1, -0.05, 0.08, 1.5, 0.15, 0.15],
}


def compare_hypotheses(w: List[float]) -> str:
    """Compara a hipótese encontrada com as opções fornecidas e retorna a mais próxima.

    Args:
        w (List[float]): Vetor de pesos encontrado.

    Returns:
        str: A opção mais próxima.
    """
    best_match = ""
    best_score = float("-inf")

    for key, hypothesis in HYPOTHESES.items():
        score = sum(
            1 if sign(sum(h * w_i for h, w_i in zip(hypothesis, w))) == sign(w_i) else 0
            for w_i in w
        )
        if score > best_score:
            best_score = score
            best_match = key

    return best_match


def run() -> None:
    """Executa o experimento para encontrar a hipótese mais próxima usando transformação não linear."""
    n_runs = 1000
    n_points = 1000
    closest_matches = {key: 0 for key in HYPOTHESES.keys()}

    for i in range(n_runs):
        print(
            Color.text(
                f"Executando iteração {i + 1} de {n_runs}...", Color.BRIGHT_YELLOW
            ),
            end="\r",
            flush=True,
        )
        X, y = generate_data_with_noise(n_points=n_points, noise_percentage=0.1)
        X_transformed = transform_features(X)

        model = LinearRegression()
        model.fit(X_transformed, y)

        best_match = compare_hypotheses(model.weights)
        closest_matches[best_match] += 1

    most_frequent_match = max(closest_matches, key=closest_matches.__getitem__)

    print(
        Color.text(
            f"\nA hipótese mais próxima em média é: {most_frequent_match}) com {closest_matches[most_frequent_match]} aparições.",
            Color.BRIGHT_CYAN,
        )
    )


if __name__ == "__main__":
    run()
