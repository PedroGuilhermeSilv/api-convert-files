from dataclasses import dataclass
from typing import Any


@dataclass
class InputConverter:
    typeInput: str
    typeOutput: str
    file: Any
