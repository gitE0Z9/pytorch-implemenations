from typing import Any
from torch import nn

from ..ghostnet.model import GhostNet
from .network import GhostLayerV2


class GhostNetV2(GhostNet):
    def __init__(
        self,
        input_channel: int = 3,
        output_size: int = 1,
        width_multiplier: float = 1,
    ):
        """GhostNet version 2 [2211.12905v1]

        Args:
            input_channel (int): input channel size. Defaults to 3.
            output_size (int, optional): output size. Defaults to 1.
            width_multiplier (float, optional): width multiplier alpha. Defaults to 1.
        """
        self.width_multiplier = width_multiplier
        super().__init__(input_channel, output_size)

    @property
    def config(self) -> list[list[Any]]:
        cfg = super().config
        # kernel: 5 -> 3 in stage 4
        for layer_idx in range(5, 11):
            layer_cfg = list(cfg[layer_idx])
            layer_cfg[2] = 3
            cfg[layer_idx] = layer_cfg

        return cfg

    def build_blocks(self):
        self.blocks = nn.Sequential(
            *[
                GhostLayerV2(
                    int(in_c * self.width_multiplier),
                    int(out_c * self.width_multiplier),
                    kernel,
                    stride=stride,
                    s=2,
                    d=3,
                    expansion_size=expansion_size,
                    enable_se=enable_se,
                    horizontal_kernel=5,
                    vertical_kernel=5,
                )
                for in_c, out_c, kernel, stride, expansion_size, enable_se in self.config
            ]
        )
