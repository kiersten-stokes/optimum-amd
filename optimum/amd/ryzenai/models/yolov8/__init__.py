# Copyright 2023 The HuggingFace Team. All rights reserved.
# Licensed under the MIT License.

from typing import TYPE_CHECKING

from transformers.utils import _LazyModule


_import_structure = {
    "image_processing_yolov8": ["YoloV8ImageProcessor"],
}

# Direct imports for type-checking
if TYPE_CHECKING:
    from .image_processing_yolov8 import YoloV8ImageProcessor
else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
