from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apyscript.display.sprite import Sprite
from apyscript.display.stage import Stage
from tests import testing_helper


class TestGraphicsClearInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_clear(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#000')
        sprite.graphics.line_style(color='#aaa')

        expected_attrs: Dict[str, Any] = {
            '_fill_color': None,
            '_fill_alpha': None,
            '_line_color': None,
            '_line_thickness': None,
            '_line_alpha': None,
        }
        sprite.graphics.clear()
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs,
            any_obj=sprite.graphics)
        assert len(sprite.graphics._childs) == 0
