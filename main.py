import importlib
from argparse import ArgumentParser, Namespace

from utils import Color, clear_screen, print_divider


def parse_arguments() -> Namespace:
    """Parsa os argumentos da linha de comando.

    Returns:
        args (Namespace): Os argumentos parseados.
    """
    parser = ArgumentParser(
        description="Execute dinamicamente um exercício específico."
    )

    parser.add_argument(
        "-l",
        "--list",
        required=True,
        type=int,
        help="Número da lista, por exemplo, '1' para 'lista1'.",
    )

    parser.add_argument(
        "-e",
        "--exercise",
        required=True,
        type=int,
        help="Número do exercício, por exemplo, '7' para 'exercicio7'.",
    )

    parser.add_argument(
        "-r",
        "--repetitions",
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


def import_exercise_module(list_num: int, exercise_num: int):
    """Importa o módulo do exercício especificado.

    Args:
        list_num (int): Número da lista.
        exercise_num (int): Número do exercício.

    Returns:
        module: Módulo importado.

    Raises:
        ImportError: Se o módulo não puder ser importado.
    """
    exercise_path = f"lista{list_num}.exercicio{exercise_num}"
    try:
        module = importlib.import_module(exercise_path)
    except ImportError as e:
        print(Color.text(f"Erro ao importar o módulo {exercise_path}: {e}", Color.RED))
        raise
    return module


def print_execution_start_message(
    list_num: int, exercise_num: int, repetitions: int
) -> None:
    """Imprime a mensagem inicial de execução.

    Args:
        list_num (int): Número da lista.
        exercise_num (int): Número do exercício.
        repetitions (int): Quantas vezes o exercício será repetido.
    """
    msg = (
        f"{Color.text('Executando o', Color.ORANGE)} "
        f"{Color.text(f'exercício {exercise_num}', Color.GREEN)} "
        f"{Color.text('da', Color.ORANGE)} "
        f"{Color.text(f'lista {list_num}', Color.BLUE)}..."
    )
    print(msg)
    print_divider()
    if repetitions > 1:
        print(
            Color.text(
                f"{Color.text('O exercício será executado', Color.MAGENTA)} "
                f"{Color.text(str(repetitions), Color.GREEN)} "
                f"{Color.text('vezes', Color.MAGENTA)}.\n",
                Color.CYAN,
            )
        )


def execute_exercise(module, repetitions: int) -> None:
    """Executa o exercício a partir do módulo importado, exibindo as instruções.

    Args:
        module: Módulo importado do exercício.
        repetitions (int): Número de repetições da execução.
    """
    statement = getattr(module, "INSTRUCTIONS", None)

    if statement:
        print(Color.text("Instruções:", Color.CYAN))
        print(Color.text(statement, Color.WHITE))
        print_divider()

    for i in range(repetitions):
        if repetitions > 1:
            execution_msg = (
                f"\n{Color.text('Execução', Color.MAGENTA)} "
                f"{Color.text(str(i + 1), Color.YELLOW)} "
                f"{Color.text('de', Color.MAGENTA)} "
                f"{Color.text(str(repetitions), Color.GREEN)}:"
            )
            print(execution_msg, end="\n\n")
            print_divider()

        module.run()
        print_divider()


def main() -> None:
    """Função principal que executa o fluxo do programa."""
    args = parse_arguments()

    if args.clear:
        clear_screen()

    list_num = args.list
    exercise_num = args.exercise

    print_execution_start_message(list_num, exercise_num, args.repetitions)

    module = import_exercise_module(list_num, exercise_num)
    execute_exercise(module, args.repetitions)


if __name__ == "__main__":
    main()
