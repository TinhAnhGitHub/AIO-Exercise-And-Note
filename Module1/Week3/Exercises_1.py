import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor


class Softmax(nn.Module):
    def __init__(self) -> None:
        super(Softmax, self).__init__()

    def forward(self, x: Tensor) -> Tensor:
        """_summary_

        Args:
            x (Tensor): input tensor 1D

        Returns:
            Tensor: return the softmax tensor 1D

        """
        result: Tensor = torch.exp(
            # dim= -1 means consider the last dimension
            x) / torch.sum(torch.exp(x), dim=-1, keepdim=True)
        return result

class SoftmaxStable(nn.Module):
    def __init__(self) -> None:
        super(SoftmaxStable, self).__init__()

    def forward(self, x: Tensor) -> Tensor:
        c: Tensor = torch.max(x)
        result: Tensor = torch.exp(x - c) / torch.sum(torch.exp(x - c), dim=-1, keepdim=True)
        return result
    

