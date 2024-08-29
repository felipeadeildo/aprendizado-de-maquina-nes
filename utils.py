import os
import shutil

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
    ORANGE = "\033[38;5;214m"  # Simulação de laranja com ANSI
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


def print_divider(char: str = "-", length: int = 80, **kwargs):
    """Imprime um separador de linha preenchido com o caractere especificado.

    Args:
        char (str): O caractere usado para preencher a linha.
        length (int): O comprimento da linha do terminal. Por padrão, usa a largura atual do terminal.
    """
    terminal_width = shutil.get_terminal_size((length, 0)).columns
    print(Color.text(char * terminal_width, Color.CYAN), **kwargs)


def clear_screen():
    """Limpa a tela do terminal."""
    os.system(CMD_CLEAR)
