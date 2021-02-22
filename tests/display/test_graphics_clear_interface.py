from random import randint
from typing import Any, Dict

from retrying import retry

from apyscript.display.graphics_clear_interface import GraphicsClearInterface
from apyscript.display.stage import Stage
from apyscript.display.sprite import Sprite
from apyscript.display.rectangle import Rectangle
from tests import testing_helper


class TestGraphicsClearInterface:

    @retry(stop_max_attempt_number=5, wait_fixed=randint(100, 1000))
    def test_clear(self) -> None:
        graphics_clear_interface: GraphicsClearInterface = \
            GraphicsClearInterface()
        graphics_clear_interface._fill_color = '#000000'
        graphics_clear_interface._fill_alpha = 0.5
        graphics_clear_interface._line_thickness = 2
        graphics_clear_interface._line_alpha = 0.3
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#000000')
        rectangle: Rectangle = sprite.graphics.draw_rect(
            x=50, y=50, width=100, height=100)
        graphics_clear_interface._graphics = [rectangle]

        expected_attrs: Dict[str, Any] = {
            '_fill_color': None,
            '_fill_alpha': None,
            '_line_color': None,
            '_line_thickness': None,
            '_line_alpha': None,
            '_graphics': [],
        }
        graphics_clear_interface.clear()
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs,
            any_obj=graphics_clear_interface)
