from .basic import PSMNet as basic
from .stackhourglass import PSMNet as stackhourglass
import torch

default_device = torch.device('cpu')
