import torch
import torch.nn as nn
from torchtyping import TensorType

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # convert from string to integer
        # add all strings to a set
        # map all strings with index
        setters = set()
        for sentence in positive:
            for word in sentence.split():
                setters.add(word)
        for sentence in negative:
            for word in sentence.split():
                setters.add(word)

        sorted_list = sorted(list(setters))
        mapping = {}
        for i in range(len(sorted_list)):
            mapping[sorted_list[i]] = i + 1

        final = []
        for sentence in positive:
            res = []
            for word in sentence.split():
                res.append(mapping[word])
            final.append(torch.tensor(res))
        for sentence in negative:
            res = []
            for word in sentence.split():
                res.append(mapping[word])
            final.append(torch.tensor(res))
        return torch.nn.utils.rnn.pad_sequence(final, batch_first=True)