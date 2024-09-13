from dataclasses import dataclass


@dataclass
class InputConverter:
    typeInput: str
    typeOutput: str
    pathFile: str