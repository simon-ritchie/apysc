from random import randint
from typing import Any
from typing import Dict

from retrying import retry

from apysc import Sprite
from apysc import Stage
from apysc import LineCaps, LineJoints, LineDotSetting
from tests import testing_helper


class TestGraphicsClearInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_clear(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#000')
        sprite.graphics.line_style(
            color='#aaa', cap=LineCaps.ROUND, joints=LineJoints.BEVEL,
            dot_setting=LineDotSetting(dot_size=10))

        expected_attrs: Dict[str, Any] = {
            '_fill_color': '',
            '_fill_alpha': 1.0,
            '_line_color': '',
            '_line_thickness': 1,
            '_line_alpha': 1.0,
            '_current_line': None,
            '_line_cap': LineCaps.BUTT.value,
            '_line_joints': LineJoints.MITER.value,
            '_line_dot_setting': None,
            '_line_dash_setting': None,
        }
        sprite.graphics.clear()
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs,
            any_obj=sprite.graphics)
        assert sprite.num_children == 0
