from string import ascii_lowercase

from linear_regression import LinearRegression
from utils import Color, generate_data_with_noise, without_transformation

INSTRUCTIONS = (
    f"{Color.text('Para obter uma estimativa confiável do erro de classificação in-sample (E_in), ', Color.BRIGHT_CYAN)}"
    f"{Color.text('você deve realizar a Regressão Linear sem transformação, ou seja, usando o vetor de características ', Color.BRIGHT_CYAN)}"
    f"{Color.text('(1, x1, x2).', Color.BRIGHT_RED)}\n\n"
    f"{Color.text('8. Qual é o valor mais próximo do erro de classificação in-sample E_in? ', Color.BRIGHT_BLUE)}"
    f"{Color.text('Execute o experimento 1000 vezes e tire a média de E_in para reduzir a variação nos seus resultados.', Color.BRIGHT_BLUE)}\n"
    f"{Color.text('Escolha a opção mais próxima do seu resultado:', Color.BRIGHT_PURPLE)}\n"
    f"{Color.text('[a] 0', Color.TEAL)}\n"
    f"{Color.text('[b] 0.1', Color.TEAL)}\n"
    f"{Color.text('[c] 0.3', Color.TEAL)}\n"
    f"{Color.text('[d] 0.5', Color.TEAL)}\n"
    f"{Color.text('[e] 0.8', Color.TEAL)}"
)


def run() -> None:
    """Executa o experimento para calcular o erro médio in-sample (E_in) utilizando Regressão Linear."""
    n_runs = 1000
    n_points = 1000
    total_e_in = 0.0

    for i in range(n_runs):
        print(
            Color.text(
                f"Executando iteração {i + 1} de {n_runs}...", Color.BRIGHT_YELLOW
            ),
            end="\r",
            flush=True,
        )
        X, y = generate_data_with_noise(n_points=n_points, noise_percentage=0.1)
        X_transformed = without_transformation(X)

        model = LinearRegression()
        model.fit(X_transformed, y)
        predictions = model.predict(X_transformed)

        # Calcular o erro E_in (erro in-sample)
        e_in = (
            sum(1 for pred, actual in zip(predictions, y) if pred != actual) / n_points
        )
        total_e_in += e_in

    average_e_in = total_e_in / n_runs

    print(
        Color.text(
            f"\nMédia de E_in (erro in-sample) após {n_runs} execuções: {average_e_in:.3f}",
            Color.BRIGHT_CYAN,
        )
    )

    alternatives_e_in = zip(ascii_lowercase[:5], [0, 0.1, 0.3, 0.5, 0.8])
    closest_e_in = min(alternatives_e_in, key=lambda x: abs(x[1] - average_e_in))
    print(
        Color.text(
            f"Alternativa mais próxima para E_in: {closest_e_in[0]}) {closest_e_in[1]}",
            Color.GREEN,
        )
    )


if __name__ == "__main__":
    run()
