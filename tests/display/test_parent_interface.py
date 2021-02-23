from random import randint

from retrying import retry

from apyscript.display.parent_interface import ParentInterface
from apyscript.display.stage import Stage
from apyscript.display.sprite import Sprite


class TestParentInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_parent(self) -> None:
        parent_interface: ParentInterface = ParentInterface()
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        parent_interface.parent = sprite
        assert parent_interface.parent == sprite
