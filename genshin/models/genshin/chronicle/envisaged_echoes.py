import enum
import typing

import pydantic

from genshin.models.model import Aliased, APIModel

__all__ = [
    "EnvisagedEchoStatus",
    "EnvisagedEcho",
    "EnvisagedEchoes",
]


class EnvisagedEchoStatus(enum.IntEnum):
    """Status of an envisaged echo."""

    LOCKED = 1
    UNLOCKED = 2
    COMPLETED = 3


class EnvisagedEcho(APIModel):

    character_id: int = Aliased("avatar_id")
    name: str
    icon: str
    status: EnvisagedEchoStatus
    has_red_dot: bool
    level_id: int


class EnvisagedEchoes(APIModel):
    """Pair of both current and previous spiral abyss.

    This may not be a namedtuple due to how pydantic handles them.
    """

    characters: typing.Sequence[EnvisagedEcho]
    is_unlocked: bool = Aliased("is_unlock")
