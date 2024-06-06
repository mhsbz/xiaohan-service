import os
import time
from ..utils import utils


class User:
    _member_id: str
    _uid: int
    level: int = 1
    name: str
    rank: int
    hp: int = 100
    mp: int = 100
    int_rank: int
    power: int

    def __init__(self, member_id: str):
        self._member_id = member_id
        self._uid = int(os.getpid()) * int(time.time())
        self.name = utils.generate_random_chinese()
