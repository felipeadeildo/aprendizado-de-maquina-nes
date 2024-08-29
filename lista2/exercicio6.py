import itertools
from typing import Callable, Dict, List, Literal, Tuple

# Contexto:
#
# Pontuação = (Número de funções alvo que concordam com a hipótese em todos os 3 pontos) × 3 +
#             (Número de funções alvo que concordam com a hipótese em exatamente 2 pontos) × 2 +
#             (Número de funções alvo que concordam com a hipótese em exatamente 1 ponto) × 1 +
#             (Número de funções alvo que concordam com a hipótese em 0 pontos) × 0.
#
# 6. Qual hipótese g concorda mais com as possíveis funções alvo em termos da pontuação acima?
#
# a) g(x) = 1
# b) g(x) = 0
# c) g é a função XOR, ou seja, g(x) = 1 se o número de 1s em x for ímpar, caso contrário g(x) = 0
# d) g é o oposto da função XOR, ou seja, g(x) = 1 se o número de 1s em x for par, caso contrário g(x) = 0
# e) Elas são todas equivalentes (mesma pontuação para g em [a] até [d]).

T = Literal[1, 0]

# Definição dos pontos não observados (101, 110, 111)
pontos_nao_observados: List[Tuple[T, T, T]] = [
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1),
]

# Geração das funções alvo possíveis (8 combinações de 0s e 1s para os 3 pontos não observados)
funcoes_alvos: List[Tuple[T, ...]] = list(itertools.product([0, 1], repeat=3))


# Definição das hipóteses
def g_a(x: Tuple[T, T, T]) -> T:
    """Hipótese g_a: retorna 1 para todos os três pontos."""
    return 1


def g_b(x: Tuple[T, T, T]) -> T:
    """Hipótese g_b: retorna 0 para todos os três pontos."""
    return 0


def g_c(x: Tuple[T, T, T]) -> T:
    """Hipótese g_c: aplica a função XOR, retorna 1 se o número de 1s for ímpar."""
    # sim, poderia só mandar `sum(x) % 2` porém, o typechecker reclama
    return 1 if sum(x) % 2 != 0 else 0


def g_d(x: Tuple[T, T, T]) -> T:
    """Hipótese g_d: oposto da função XOR, retorna 1 se o número de 1s for par."""
    return 0 if sum(x) % 2 != 0 else 1


# Função para calcular a pontuação de uma hipótese
def calcula_scores(hipotese: Callable[[Tuple[T, T, T]], T]) -> int:
    """Calcula a pontuação da hipótese com base na concordância com as funções alvo possíveis."""
    scores = [0, 0, 0, 0]  # Contador para concordância em 3, 2, 1, 0 pontos

    for fn in funcoes_alvos:
        concordancia = 0
        for i, ponto in enumerate(pontos_nao_observados):
            if hipotese(ponto) == fn[i]:
                concordancia += 1

        scores[concordancia] += 1

    # Cálculo da pontuação final com base nas concordâncias
    final_score = sum(scores[i] * i for i in range(4))
    return final_score


# Definição das hipóteses
hipoteses: Dict[str, Callable[[Tuple[T, T, T]], T]] = {
    "g_a": g_a,
    "g_b": g_b,
    "g_c": g_c,
    "g_d": g_d,
}


def run() -> None:
    scores: Dict[str, int] = {}

    print("Calculando as pontuações para cada hipótese...\n")

    for nome, hipotese in hipoteses.items():
        score = calcula_scores(hipotese)
        scores[nome] = score
        print(f"Pontuação de {nome}(x): {score}")

    scores_set = set(scores.values())
    if len(scores_set) == 1:
        print(
            "\nTodas as hipóteses têm a mesma pontuação. Resposta: e) Elas são todas equivalentes."
        )
    else:
        melhor_hipotese = max(scores, key=scores.__getitem__)
        print(
            f"\nA melhor hipótese é {melhor_hipotese} com pontuação {scores[melhor_hipotese]}."
        )


if __name__ == "__main__":
    run()
