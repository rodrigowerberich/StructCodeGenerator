from enum import Enum


class LineTypes(Enum):
    COMMENT = 1,
    MESSAGE_START = 2,
    MESSAGE_FIELD = 3,
    MESSAGE_END = 4
