from random import randint

from retrying import retry

import apysc as ap
from apysc._display.rectangle import Rectangle
from apysc._testing import testing_helper


class TestGraphicsBase:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test___init__(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        
