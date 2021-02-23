from random import randint

from retrying import retry

from apyscript.display.child_interface import ChildInterface
from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage


class TestChildInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_add_child(self) -> None:
        interface: ChildInterface = ChildInterface()
        interface._childs = []
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        interface.add_child(child=sprite)
        assert interface._childs == [sprite]
