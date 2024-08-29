from string import ascii_lowercase

from perceptron import Perceptron
from utils import generate_data

INSTRUCTIONS = """
Para obter uma estimativa confiável dessas duas quantidades, você deve repetir o experimento
1000 vezes (cada execução conforme especificado acima) e calcular a média sobre essas execuções.

7. Considere N = 10. Quantas iterações, em média, são necessárias para que o PLA converja
com N = 10 pontos de treinamento? Escolha o valor mais próximo dos seus resultados.
('mais próximo' significa: |sua resposta - opção dada| é a mais próxima de 0).
""".strip()


def run() -> None:
    n_runs = 1000
    total_iterations = 0
    n_points = 10

    for i in range(n_runs):
        print(f"Executando iteração {i + 1} de {n_runs}...", end="\r", flush=True)
        X, y = generate_data(n_points)
        pla = Perceptron(n_iters=1000)
        pla.fit(X, y)
        total_iterations += pla.iterations

    average_iterations = total_iterations / n_runs

    print(
        f"\nMédia de iterações para convergência com N = {n_points}: {average_iterations}"
    )

    alternatives = zip(ascii_lowercase, [1, 15, 300, 5000, 10000])
    closest = min(alternatives, key=lambda x: abs(x[1] - average_iterations))
    print(f"Alternativa mais próxima: {closest[0]}) com {closest[1]} iterações")


if __name__ == "__main__":
    run()
