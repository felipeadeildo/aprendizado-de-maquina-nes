from typing import List

from utils import (
    matrix_inverse,
    matrix_multiply,
    matrix_vector_multiply,
    sign,
    transpose,
)

#  TODO: add docstrings to all methods


class LinearRegression:
    def __init__(self) -> None:
        self.weights: List[float] = []

    def fit(self, X: List[List[float]], y: List[float]) -> None:
        X_T = transpose(X)
        X_T_X = matrix_multiply(X_T, X)
        X_T_X_inv = matrix_inverse(X_T_X)
        X_T_y = matrix_vector_multiply(X_T, y)
        self.weights = matrix_vector_multiply(X_T_X_inv, X_T_y)

    def predict(self, X: List[List[float]]) -> List[float]:
        return [
            sign(sum(self.weights[j] * x_i[j] for j in range(len(self.weights))))
            for x_i in X
        ]
