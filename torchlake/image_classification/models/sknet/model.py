from ..resnext.model import ResNeXt
from .network import BottleNeck

# input, output, base?, number_block, block_type
CONFIGS = {
    26: [
        [64, 256, 128, 2, BottleNeck],  # less block
        [256, 512, 256, 2, BottleNeck],  # less block
        [512, 1024, 512, 2, BottleNeck],  # less block
        [1024, 2048, 1024, 2, BottleNeck],  # less block
    ],
    50: [
        [64, 256, 128, 3, BottleNeck],
        [256, 512, 256, 4, BottleNeck],
        [512, 1024, 512, 6, BottleNeck],
        [1024, 2048, 1024, 3, BottleNeck],
    ],
    101: [
        [64, 256, 128, 3, BottleNeck],
        [256, 512, 256, 4, BottleNeck],
        [512, 1024, 512, 23, BottleNeck],  # more block
        [1024, 2048, 1024, 3, BottleNeck],
    ],
    152: [
        [64, 256, 128, 3, BottleNeck],
        [256, 512, 256, 8, BottleNeck],  # more block
        [512, 1024, 512, 36, BottleNeck],  # more block
        [1024, 2048, 1024, 3, BottleNeck],
    ],
}


class SkNet(ResNeXt):
    configs = CONFIGS
