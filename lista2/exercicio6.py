import itertools
from typing import Callable, Dict, List, Literal, Tuple

INSTRUCTIONS = """
Pontuação = (Número de funções alvo que concordam com a hipótese em todos os 3 pontos) × 3 +
            (Número de funções alvo que concordam com a hipótese em exatamente 2 pontos) × 2 +
            (Número de funções alvo que concordam com a hipótese em exatamente 1 ponto) × 1 +
            (Número de funções alvo que concordam com a hipótese em 0 pontos) × 0.

6. Qual hipótese g concorda mais com as possíveis funções alvo em termos da pontuação acima?

a) g(x) = 1
b) g(x) = 0
c) g é a função XOR, ou seja, g(x) = 1 se o número de 1s em x for ímpar, caso contrário g(x) = 0
d) g é o oposto da função XOR, ou seja, g(x) = 1 se o número de 1s em x for par, caso contrário g(x) = 0
e) Elas são todas equivalentes (mesma pontuação para g em [a] até [d]).
""".strip()

T = Literal[1, 0]

# Definição dos pontos não observados (101, 110, 111)
unobserved_points: List[Tuple[T, T, T]] = [
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
]

# Geração das funções alvo possíveis (8 combinações de 0s e 1s para os 3 pontos não observados)
target_functions: List[Tuple[T, ...]] = list(itertools.product([0, 1], repeat=3))


def hypothesis_a(x: Tuple[T, T, T]) -> T:
    """Hipótese g_a: retorna 1 para todos os três pontos.

    Args:
        x (Tuple[T, T, T]): Um ponto.

    Returns:
        T: O valor da hipótese g_a.
    """
    return 1


def hypothesis_b(x: Tuple[T, T, T]) -> T:
    """Hipótese g_b: retorna 0 para todos os três pontos.

    Args:
        x (Tuple[T, T, T]): Um ponto.

    Returns:
        T: O valor da hipótese g_b.
    """
    return 0


def hypothesis_c(x: Tuple[T, T, T]) -> T:
    """Hipótese g_c: aplica a função XOR, retorna 1 se o número de 1s for ímpar.

    Args:
        x (Tuple[T, T, T]): Um ponto.

    Returns:
        T: O valor da hipótese g_c.
    """
    return 1 if sum(x) % 2 != 0 else 0


def hypothesis_d(x: Tuple[T, T, T]) -> T:
    """Hipótese g_d: oposto da função XOR, retorna 1 se o número de 1s for par.

    Args:
        x (Tuple[T, T, T]): Um ponto.

    Returns:
        T: O valor da hipótese g_d.
    """
    return 0 if sum(x) % 2 != 0 else 1


def calculate_scores(hypothesis: Callable[[Tuple[T, T, T]], T]) -> int:
    """Calcula a pontuação da hipótese com base na concordância com as funções alvo possíveis.

    Args:
        hypothesis (Callable[[Tuple[T, T, T]], T]): A hipótese a ser avaliada.

    Returns:
        int: A pontuação da hipótese.
    """
    scores = [0, 0, 0, 0]  # Contador para concordância em 3, 2, 1, 0 pontos

    for fn in target_functions:
        agreement = 0
        for i, point in enumerate(unobserved_points):
            if hypothesis(point) == fn[i]:
                agreement += 1

        scores[agreement] += 1

    final_score = sum(scores[i] * i for i in range(4))
    return final_score


hypotheses: Dict[str, Callable[[Tuple[T, T, T]], T]] = {
    "g_a": hypothesis_a,
    "g_b": hypothesis_b,
    "g_c": hypothesis_c,
    "g_d": hypothesis_d,
}


def run() -> None:
    """Calcula as pontuações para cada hipótese e exibe o resultado."""
    print("Calculando as pontuações para cada hipótese...\n")

    scores: Dict[str, int] = {}

    for name, hypothesis in hypotheses.items():
        score = calculate_scores(hypothesis)
        scores[name] = score
        print(f"Pontuação de {name}(x): {score}")

    scores_set = set(scores.values())
    if len(scores_set) == 1:
        print(
            "\nTodas as hipóteses têm a mesma pontuação. Resposta: e) Elas são todas equivalentes."
        )
    else:
        best_hypothesis = max(scores, key=scores.__getitem__)
        print(
            f"\nA melhor hipótese é {best_hypothesis} com pontuação {scores[best_hypothesis]}."
        )


if __name__ == "__main__":
    run()
