import numpy as np
from numpy.typing import NDArray


# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # prediction is just weights times dataset
        out = X@weights
        return np.round(out, 5)



    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # mean squared error
        # its just model - truth squared times mean

        truth = model_prediction - ground_truth
        squared = np.square(truth)
        mean = np.mean(squared)
        return round(np.mean(squared), 5)