import os
import random
import shutil
from typing import List, Tuple, Union

from constants import CMD_CLEAR


class Color:
    """Classe para adicionar e remover cores nas mensagens do terminal."""

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    ORANGE = "\033[38;5;214m"
    BLACK = "\033[30m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    GRAY = "\033[90m"
    BRIGHT_ORANGE = "\033[38;5;202m"
    PURPLE = "\033[38;5;129m"
    BRIGHT_PURPLE = "\033[38;5;165m"
    TEAL = "\033[38;5;43m"
    BRIGHT_TEAL = "\033[38;5;80m"
    RESET = "\033[0m"

    @classmethod
    def text(cls, text: str, color: str) -> str:
        """Retorna o texto com a cor aplicada.

        Args:
            text (str): O texto a ser colorido.
            color (str): O código da cor a ser aplicado.

        Returns:
            str: O texto colorido.
        """
        return f"{color}{text}{cls.RESET}"


def print_divider(char: str = "-", length: int = 80, **kwargs) -> None:
    """Imprime um separador de linha preenchido com o caractere especificado.

    Args:
        char (str): O caractere usado para preencher a linha.
        length (int): O comprimento da linha do terminal. Por padrão, usa a largura atual do terminal.
    """
    terminal_width = shutil.get_terminal_size((length, 0)).columns
    print(Color.text(char * terminal_width, Color.CYAN), **kwargs)


def clear_screen() -> None:
    """Limpa a tela do terminal."""
    os.system(CMD_CLEAR)


def generate_data(n_points: int = 10, interval: tuple[float, float] = (-1, 1)) -> tuple:
    """Gera os dados de treinamento e a função alvo.

    Args:
        n_points (int): Número de pontos de dados a serem gerados.
        interval (tuple[float, float]): Intervalo para geração dos valores dos pontos.

    Returns:
        tuple: Uma tupla contendo a matriz de características (X) e o vetor de rótulos (y).
    """
    X = [[random.uniform(*interval) for _ in range(2)] for _ in range(n_points)]
    point1 = [random.uniform(*interval) for _ in range(2)]
    point2 = [random.uniform(*interval) for _ in range(2)]

    def target_function(x: List[float]) -> int:
        """Calcula a função alvo baseada na linha.

        Args:
            x (List[float]): Uma lista representando um ponto.

        Returns:
            int: O rótulo predito para o ponto (1 ou -1).
        """
        return (
            1
            if (x[1] - point1[1]) * (point2[0] - point1[0])
            > (point2[1] - point1[1]) * (x[0] - point1[0])
            else -1
        )

    y: List[Union[float, int]] = [target_function(x) for x in X]
    return X, y


def evaluate_target_function(
    point1: List[float], point2: List[float], x: List[float]
) -> int:
    """Avalia a função alvo f(x) em um ponto x.

    Args:
        point1 (List[float]): Primeiro ponto que define a função alvo.
        point2 (List[float]): Segundo ponto que define a função alvo.
        x (List[float]): Ponto a ser classificado.

    Returns:
        int: +1 ou -1 dependendo de que lado da linha o ponto x se encontra.
    """
    return (
        1
        if (x[1] - point1[1]) * (point2[0] - point1[0])
        > (point2[1] - point1[1]) * (x[0] - point1[0])
        else -1
    )


def generate_target_function(
    interval: Tuple[float, float] = (-1, 1),
) -> Tuple[List[float], List[float]]:
    """Gera uma função alvo f(x) aleatória.

    Args:
        interval (Tuple[float, float]): Intervalo para geração dos valores dos pontos.

    Returns:
        Tuple[List[float], List[float]]: Dois pontos que definem a função alvo.
    """
    point1 = [random.uniform(*interval) for _ in range(2)]
    point2 = [random.uniform(*interval) for _ in range(2)]
    return point1, point2


def sign(x: float) -> int:
    """Retorna o sinal de x.

    Args:
        x (float): Valor a ser avaliado.

    Returns:
        int: 1 se x >= 0, -1 se x < 0.
    """
    return 1 if x >= 0 else -1


def generate_data_with_noise(
    *,
    n_points: int = 10,
    interval: Tuple[float, float] = (-1, 1),
    noise: float = 0.1,
    noise_percentage: float = 0.1,
) -> Tuple[List[List[float]], List[Union[float, int]]]:
    """Gera os dados de treinamento com base na função alvo e adiciona ruído.

    Args:
        n_points (int): Número de pontos de dados a serem gerados.
        interval (Tuple[float, float]): Intervalo para geração dos valores dos pontos.
        noise (float): Intensidade do ruido.
        noise_percentage (float): Porcentagem dos dados que serão ruidosos.

    Returns:
        Tuple[List[List[float]], List[Union[float, int]]]: Matriz de características (X) e vetor de rótulos (y).
    """
    X, y = generate_data(n_points, interval)

    n_noise = int(noise_percentage * n_points)
    noise_indices = random.sample(range(n_points), n_noise)
    for i in noise_indices:
        # TODO: verificar a forma correta de adicionar ruido
        # X[i][0] += random.uniform(-noise, noise)
        # X[i][1] += random.uniform(-noise, noise)
        y[i] *= -1
    return X, y


def transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Transpõe uma matriz.

    Args:
        matrix (List[List[float]]): Matriz a ser transposta.

    Returns:
        List[List[float]]: Matriz transposta.
    """
    return list(map(list, zip(*matrix)))


def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """Multiplica duas matrizes.

    Args:
        A (List[List[float]]): Matriz A.
        B (List[List[float]]): Matriz B.

    Returns:
        List[List[float]]: Resultado da multiplicação.
    """
    return [
        [sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A
    ]


def matrix_inverse(matrix: List[List[float]]) -> List[List[float]]:
    """Calcula a matriz inversa de uma matriz.

    Utiliza o método de escalonamento.

    Args:
        matrix (List[List[float]]): Matriz a ser invertida.

    Returns:
        List[List[float]]: Matriz inversa.
    """
    n = len(matrix)
    assert all(len(row) == n for row in matrix), "Matriz não é quadrada"

    A = [[element for element in row] for row in matrix]
    B = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("Matriz não tem inversa")
        for j in range(i, n):
            A[i][j] /= pivot
        for j in range(n):
            B[i][j] /= pivot
        for k in range(n):
            if i != k:
                alpha = A[k][i]
                for j in range(i, n):
                    A[k][j] -= alpha * A[i][j]
                for j in range(n):
                    B[k][j] -= alpha * B[i][j]
    return B


def matrix_vector_multiply(
    matrix: List[List[float]], vector: List[float]
) -> List[float]:
    """Multiplica uma matriz por um vetor.

    (Aplica a matriz num vetor)

    Args:
        matrix (List[List[float]]): Matriz.
        vector (List[float]): Vetor.

    Returns:
        List[float]: Resultado da multiplicação.
    """
    return [sum(m * v for m, v in zip(row, vector)) for row in matrix]


def without_transformation(X: List[List[float]]) -> List[List[float]]:
    """Retorna a matriz de entrada sem transformação.

    Args:
        X (List[List[float]]): Matriz de entrada.

    Returns:
        List[List[float]]: Matriz de entrada sem transformação.
    """
    return [[1, x1, x2] for x1, x2 in X]


def transform_features(X: List[List[float]]) -> List[List[float]]:
    """Transforma as características para o vetor não linear.

    Args:
        X (List[List[float]]): Matriz de características original.

    Returns:
        List[List[float]]: Matriz de características transformada.
    """
    return [[1, x1, x2, x1 * x2, x1**2, x2**2] for x1, x2 in X]
