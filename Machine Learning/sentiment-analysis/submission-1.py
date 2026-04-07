import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        self.layer = nn.Embedding(vocabulary_size, 16)
        # compute average of embeddings removing time dimension
        # end with a single neuron linear layer -> sigmoid

        # whole point of this is a neural network, input is a bunch of 
        # strings output is a probability distribution
        self.linear = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()
       

    def forward(self, x: TensorType[int]) -> TensorType[float]:
        # Hint: The embedding layer outputs a B, T, embed_dim tensor
        # but you should average it into a B, embed_dim tensor before using the Linear layer

        # Return a B, 1 tensor and round to 4 decimal places
        # output is. a number between 0 and 1
        embeddings = self.layer(x)
        average = torch.mean(embeddings, dim=1)
        brudda = self.linear(average)
        return torch.round(self.sigmoid(brudda), decimals=4)
