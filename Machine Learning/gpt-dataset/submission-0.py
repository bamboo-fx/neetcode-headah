import torch
from typing import List, Tuple

class Solution:
    def batch_loader(self, raw_dataset: str, context_length: int, batch_size: int) -> Tuple[List[List[str]]]:
        # You must start by generating batch_size different random indices in the appropriate range
        # using a single call to torch.randint()
        torch.manual_seed(0)
        # input is a raw dataset with the batch size and context length
        # i need to return the input data and its corresponding labeled data
        # the way this is done is buy just taking the indices and shifting by one for the labeled data

        word = raw_dataset.split()

        indices = torch.randint(low=0, high=len(word)-context_length, size=(batch_size,))

        X = []
        Y = []
        for index in indices:
            X.append(word[index: index + context_length])
            Y.append(word[index + 1: index+1+context_length])


        return X, Y


        
