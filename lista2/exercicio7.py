from string import ascii_lowercase

from perceptron import Perceptron
from utils import Color, generate_data

INSTRUCTIONS = (
    f"{Color.text('Para obter uma estimativa confiável dessas duas quantidades, você deve repetir o experimento ', Color.BRIGHT_CYAN)}"
    f"{Color.text('1000 vezes', Color.BRIGHT_RED)} "
    f"{Color.text('(cada execução conforme especificado acima) e calcular a média sobre essas execuções.', Color.BRIGHT_CYAN)}\n\n"
    f"{Color.text('7. Considere N = 10. Quantas iterações, em média, são necessárias para que o PLA converja ', Color.BRIGHT_BLUE)}"
    f"{Color.text('com N = 10 pontos de treinamento?', Color.BRIGHT_BLUE)}\n"
    f"{Color.text('Escolha o valor mais próximo dos seus resultados.', Color.BRIGHT_PURPLE)}\n"
    f"{Color.text('(\'mais próximo\' significa: |sua resposta - opção dada| é a mais próxima de 0).', Color.TEAL)}"
)


def run() -> None:
    """Executa o experimento para calcular o número médio de iterações até a convergência do PLA."""
    n_runs = 1000
    total_iterations = 0
    n_points = 10

    for i in range(n_runs):
        print(
            Color.text(
                f"Executando iteração {i + 1} de {n_runs}...", Color.BRIGHT_YELLOW
            ),
            end="\r",
            flush=True,
        )
        X, y = generate_data(n_points)
        pla = Perceptron(n_iters=1000)
        pla.fit(X, y)
        total_iterations += pla.iterations

    average_iterations = total_iterations / n_runs

    print(
        Color.text(
            f"\nMédia de iterações para convergência com N = {n_points}: {average_iterations}",
            Color.BRIGHT_CYAN,
        )
    )

    alternatives = zip(ascii_lowercase, [1, 15, 300, 5000, 10000])
    closest = min(alternatives, key=lambda x: abs(x[1] - average_iterations))
    print(
        Color.text(
            f"Alternativa mais próxima: {closest[0]}) com {closest[1]} iterações",
            Color.GREEN,
        )
    )


if __name__ == "__main__":
    run()
