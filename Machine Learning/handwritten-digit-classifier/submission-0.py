import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        # architecture
        self.first_layer = nn.Linear(784, 512)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.2)
        self.final_layer = nn.Linear(512, 10)
        self.sigmoid = nn.Sigmoid()
        
    
    def forward(self, images: TensorType[float]) -> TensorType[float]:
        torch.manual_seed(0)
        # Return the model's prediction to 4 decimal places

        # data flow through nn

        res = self.first_layer(images)
        ress = self.relu(res)
        resss = self.dropout(ress)
        ressss = self.final_layer(resss)
        resssss = self.sigmoid(ressss)

        return torch.round(resssss, decimals=4)