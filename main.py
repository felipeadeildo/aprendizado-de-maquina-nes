import importlib
from argparse import ArgumentParser

from utils import Color, clear_screen, print_divider


def parse_arguments():
    """Parsa os argumentos da linha de comando."""
    parser = ArgumentParser(
        description="Execute dinamicamente um exercício específico."
    )

    parser.add_argument(
        "-l",
        "--lista",
        required=True,
        type=int,
        help="Número da lista, por exemplo, '1' para 'lista1'.",
    )

    parser.add_argument(
        "-e",
        "--exercicio",
        required=True,
        type=int,
        help="Número do exercício, por exemplo, '7' para 'exercicio7'.",
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


def import_exercise_module(lista_num: int, exercicio_num: int):
    """Importa o módulo do exercício especificado."""
    exercise_path = f"lista{lista_num}.exercicio{exercicio_num}"
    try:
        module = importlib.import_module(exercise_path)
    except ImportError as e:
        print(Color.text(f"Erro ao importar o módulo {exercise_path}: {e}", Color.RED))
        raise
    return module


def print_execution_start_message(lista_num: int, exercicio_num: int, repeat: int):
    """Imprime a mensagem inicial de execução."""
    msg = (
        f"{Color.text('Executando o', Color.ORANGE)} "
        f"{Color.text(f'exercício {exercicio_num}', Color.GREEN)} "
        f"{Color.text('da', Color.ORANGE)} "
        f"{Color.text(f'lista {lista_num}', Color.BLUE)}..."
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
    """Executa o exercício a partir do módulo importado, exibindo o enunciado."""
    enunciado = getattr(module, "ENUNCIADO", None)

    if enunciado:
        print(Color.text("Enunciado do Exercício:", Color.CYAN))
        print(Color.text(enunciado, Color.WHITE))
        print_divider()

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


def main():
    args = parse_arguments()

    if args.clear:
        clear_screen()

    lista_num = args.lista
    exercicio_num = args.exercicio

    print_execution_start_message(lista_num, exercicio_num, args.repeat)

    module = import_exercise_module(lista_num, exercicio_num)
    execute_exercise(module, args.repeat)


if __name__ == "__main__":
    main()
