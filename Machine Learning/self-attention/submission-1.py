import torch
import torch.nn as nn
from torchtyping import TensorType

# 0. Instantiate the linear layers in the following order: Key, Query, Value.
# 1. Biases are not used in Attention, so for all 3 nn.Linear() instances, pass in bias=False.
# 2. torch.transpose(tensor, 1, 2) returns a B x T x A tensor as a B x A x T tensor.
# 3. This function is useful:
#    https://pytorch.org/docs/stable/generated/torch.nn.functional.softmax.html
# 4. Apply the masking to the TxT scores BEFORE calling softmax() so that the future
#    tokens don't get factored in at all.
#    To do this, set the "future" indices to float('-inf') since e^(-infinity) is 0.
# 5. To implement masking, note that in PyTorch, tensor == 0 returns a same-shape tensor 
#    of booleans. Also look into utilizing torch.ones(), torch.tril(), and tensor.masked_fill(),
#    in that order.
class SingleHeadAttention(nn.Module):
    
    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        # define the self attention architecture with layers
        
        # how do we define attention
        self.key = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.query = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.value = nn.Linear(embedding_dim, attention_dim, bias=False)

    
    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        # Return your answer to 4 decimal places
        # data flow

        # torch.transpose(tensor, 1, 2) returns a B x T x A tensor as a B x A x T tensor.
        
        # find dot product of Q and K transpose to find word relationships
        # mask to only include present and past words
        # softmax to make it probability distribution
        # matrix multiplication
        # output -> B, T, A containing words in context and relationships

        # Q @ K transpose
        # mask
        # softmax
        # @ with V

        k = self.key(embedded)
        context_length, attention_dim = k.shape[1], k.shape[2]

        output = self.query(embedded)@torch.transpose(self.key(embedded), 1, 2)

        # To do this, set the "future" indices to float('-inf') since e^(-infinity) is 0.
        # 5. To implement masking, note that in PyTorch, tensor == 0 returns a same-shape tensor 
        # of booleans. Also look into utilizing torch.ones(), torch.tril(), and tensor.masked_fill(),
        # in that order.

        output = output / (attention_dim ** 0.5)
        # we need to say everywhere = 0 is true, else false
        mask = torch.tril(torch.ones((context_length, context_length)))

        brudda = mask == 0

        output = output.masked_fill(brudda, float('-inf'))

        output = nn.functional.softmax(output, dim=2)
        output = output@self.value(embedded)
        return torch.round(output, decimals=4)

