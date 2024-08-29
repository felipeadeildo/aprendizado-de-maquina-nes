import random
from typing import List


class Perceptron:
    """Algoritmo de Aprendizado Perceptron (PLA).

    Este é um classificador linear que tenta encontrar um vetor de pesos que separe
    duas classes de dados linearmente separáveis. O algoritmo ajusta os pesos
    iterativamente com base nos erros de classificação.

    A função de ativação utilizada é a função degrau, onde a saída é 1 se a soma ponderada
    das entradas for maior que 0, caso contrário, a saída é 0.

    Args:
        learning_rate (float): A taxa de aprendizado que controla o quanto os pesos são
            ajustados a cada iteração. Valor padrão é 0.01.
        n_iters (int): O número de iterações do algoritmo. Valor padrão é 1000.
    """

    weights: List[float]

    def __init__(self, learning_rate: float = 0.01, n_iters: int = 1000):
        """Inicializa o Perceptron com uma taxa de aprendizado e número de iterações.

        Args:
            learning_rate (float): A taxa de aprendizado.
            n_iters (int): O número de iterações.
        """
        self.lr = learning_rate
        self.n_iters = n_iters

    def fit(self, X: List[List[float]], y: List[float]):
        """Treina o Perceptron usando os dados de treinamento.

        Este método ajusta os pesos do Perceptron para minimizar os erros de classificação.

        Args:
            X (List[List[float]]): A matriz de características de entrada, onde cada elemento
                é uma lista que representa as características de uma amostra.
            y (List[float]): O vetor de rótulos de saída, onde cada elemento é o rótulo
                associado a uma amostra de entrada.

        A fórmula para o ajuste dos pesos é:
            w_j = w_j + η * (y_i - ŷ) * x_ij
        onde:
            w_j = peso para a característica j
            η = taxa de aprendizado (learning_rate)
            y_i = rótulo verdadeiro da amostra i
            ŷ = predição do Perceptron para a amostra i
            x_ij = valor da característica j na amostra i
        """
        self.weights = [random.random() for _ in range(len(X[0]) + 1)]

        # self.weights[0] é o bias
        X = [[1] + x for x in X]

        for _ in range(self.n_iters):
            self._update_weights(X, y)

    def _update_weights(self, X: List[List[float]], y: List[float]):
        """Atualiza os pesos do Perceptron com base nas amostras de treinamento.

        Este método percorre cada amostra de treinamento e ajusta os pesos com base no erro
        de predição.

        Args:
            X (List[List[float]]): A matriz de características de entrada, com o bias adicionado.
            y (List[float]): O vetor de rótulos de saída.

        A fórmula para o ajuste dos pesos é:
            w_j = w_j + η * (y_i - ŷ) * x_ij
        """
        # X_i := amostra de treinamento
        # y_i := rótulo da amostra de treinamento
        # w_i := peso da amostra de treinamento
        # w_n+1 := bias.

        for i in range(len(X)):
            y_hat = self.predict(X[i])

            error = y[i] - y_hat

            for j in range(len(X[i])):
                self.weights[j] += self.lr * error * X[i][j]

    def predict(self, X: List[float]) -> float:
        """Prediz o rótulo de uma amostra de entrada com base nos pesos atuais.

        Args:
            X (List[float]): Uma lista que representa as características de uma amostra.

        Returns:
            float: O rótulo predito para a amostra (1 ou 0).

        A predição é feita pela soma ponderada das características:
            z = ∑(x_ij * w_j)
        onde:
            x_ij = valor da característica j na amostra i
            w_j = peso para a característica j

        A função de ativação é então aplicada a z para determinar o rótulo predito.
        """
        z = sum(X[i] * self.weights[i] for i in range(len(X)))

        return self._activation(z)

    def _activation(self, z: float) -> float:
        """Função de ativação que aplica a função degrau.

        Args:
            z (float): A soma ponderada das entradas.

        Returns:
            float: O rótulo de saída (1 se z > 0, caso contrário 0).
        """
        return 1 if z > 0 else 0
