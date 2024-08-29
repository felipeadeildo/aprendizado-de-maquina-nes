import importlib
import os
import shutil
from argparse import ArgumentParser

CMD_CLEAR = "cls" if os.name == "nt" else "clear"
"""Comando para limpar a tela do terminal."""


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


def parse_arguments():
    """Parsa os argumentos da linha de comando."""
    parser = ArgumentParser(
        description="Execute dinamicamente um exercício específico."
    )
    parser.add_argument(
        "-e",
        "--exercise",
        required=True,
        type=str,
        help="Informe no formato 'listaX.exercicioY', por exemplo 'lista1.exercicio1'.",
    )

    parser.add_argument(
        "-r",
        "--repeat",
        type=int,
        help="Quantas vezes o exercício deve ser executado.",
        default=1,
    )

    parser.add_argument(
        "-c",
        "--clear",
        action="store_true",
        help="Limpa a tela antes de cada execução.",
    )

    return parser.parse_args()


def import_exercise_module(exercise_path: str):
    """Importa o módulo do exercício especificado."""
    try:
        module = importlib.import_module(exercise_path)
    except ImportError as e:
        print(Color.text(f"Erro ao importar o módulo {exercise_path}: {e}", Color.RED))
        raise
    return module


def print_divider(char: str = "-", length: int = 80, **kwargs):
    """Imprime um separador de linha preenchido com o caractere especificado.

    Args:
        char (str): O caractere usado para preencher a linha.
        length (int): O comprimento da linha do terminal. Por padrão, usa a largura atual do terminal.
    """
    terminal_width = shutil.get_terminal_size((length, 0)).columns
    print(Color.text(char * terminal_width, Color.CYAN), **kwargs)


def print_execution_start_message(lista: str, exercicio: str, repeat: int):
    """Imprime a mensagem inicial de execução."""
    msg = (
        f"{Color.text('Executando o', Color.ORANGE)} "
        f"{Color.text(f'exercício {exercicio.removeprefix('exercicio')}', Color.GREEN)} "
        f"{Color.text('da', Color.ORANGE)} "
        f"{Color.text(f'lista {lista.removeprefix('lista')}', Color.BLUE)}..."
    )
    print(msg)
    print_divider()
    if repeat > 1:
        print(
            Color.text(
                f"{Color.text('O exercício será executado', Color.MAGENTA)} "
                f"{Color.text(str(repeat), Color.GREEN)} "
                f"{Color.text('vezes', Color.MAGENTA)}.\n",
                Color.CYAN,
            )
        )


def execute_exercise(module, repeat: int):
    """Executa o exercício a partir do módulo importado."""
    for i in range(repeat):
        if repeat > 1:
            execution_msg = (
                f"\n{Color.text('Execução', Color.MAGENTA)} "
                f"{Color.text(str(i + 1), Color.YELLOW)} "
                f"{Color.text('de', Color.MAGENTA)} "
                f"{Color.text(str(repeat), Color.GREEN)}:"
            )
            print(execution_msg, end="\n\n")
            print_divider()

        module.run()
        print_divider()


def clear_screen():
    """Limpa a tela do terminal."""
    os.system(CMD_CLEAR)


def main():
    args = parse_arguments()

    if args.clear:
        clear_screen()
    lista, exercicio = args.exercise.split(".")

    print_execution_start_message(lista, exercicio, args.repeat)

    module = import_exercise_module(args.exercise)
    execute_exercise(module, args.repeat)


if __name__ == "__main__":
    main()
