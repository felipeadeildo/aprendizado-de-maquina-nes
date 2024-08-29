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
    n_points: int = 10, interval: tuple[float, float] = (-1, 1), noise: float = 0.1
) -> tuple:
    """Gera os dados de treinamento com base na função alvo e adiciona ruído.

    Args:
        n_points (int): Número de pontos de dados a serem gerados.

    Returns:
        Tuple[List[List[float]], List[int]]: Matriz de características (X) e vetor de rótulos (y).
    """
    X, y = generate_data(n_points, interval)
    y = [y_i + random.uniform(-noise, noise) for y_i in y]
    return X, y
