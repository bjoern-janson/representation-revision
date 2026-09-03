# boolean_world/types.py
from enum import Enum, auto

class ValueType(Enum):
    BOOL = auto()
    BIT = auto()
    INDEX = auto()
    CONTEXT = auto()

class Op(Enum):
    # Access
    INPUT = auto()
    CTX = auto()
    # Boolean operators
    NOT = auto()
    AND = auto()
    OR = auto()
    XOR = auto()
    # Value relations
    EQ = auto()
    NEQ = auto()
    # Index relations
    BEFORE = auto()
    ADJACENT = auto()

class AssayOutcome(Enum):
    REVISE = auto()
    RETAIN = auto()
    ABSTAIN = auto()
    OOU = auto()
    MODEL_MISFIT = auto()
    ERROR = auto()
