import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # take positive and negative text -> 2D tensor of int

        # make a set()
        # sort it
        # map word to index
        # iterate through make two lists and then convert to tensor
        # then add padding

        words = set()
        mapping = {}
        for sentence in positive:
            for word in sentence.split():
                words.add(word)
        for sentence in negative:
            for word in sentence.split():
                words.add(word)

        sorted_list = sorted(list(words))
        for i in range(len(sorted_list)):
            mapping[sorted_list[i]] = i + 1

        tensor = []
        for sentence in positive:
            res = []
            for word in sentence.split():
                res.append(mapping[word])
            tensor.append(torch.tensor(res))
        for sentence in negative:
            res = []
            for word in sentence.split():
                res.append(mapping[word])
            tensor.append(torch.tensor(res))
        return torch.nn.utils.rnn.pad_sequence(tensor, batch_first=True)

