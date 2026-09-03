from enum import Enum, auto


class ValueType(Enum):
    BOOL = auto()
    BIT = auto()


class Op(Enum):
    INPUT = auto()
    NOT = auto()
    AND = auto()
    OR = auto()
    XOR = auto()
    EQ = auto()
    NEQ = auto()


class AssayOutcome(Enum):
    REVISE = auto()
    RETAIN = auto()
    ABSTAIN = auto()
    OOU = auto()
    MODEL_MISFIT = auto()
    ERROR = auto()
