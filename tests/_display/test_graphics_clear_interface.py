from random import randint
from typing import Any
from typing import Dict

from retrying import retry

import apysc as ap
from tests import testing_helper


class TestGraphicsClearInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_clear(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        sprite.graphics.begin_fill(color='#000')
        sprite.graphics.line_style(
            color='#aaa', cap=ap.LineCaps.ROUND, joints=ap.LineJoints.BEVEL,
            dot_setting=ap.LineDotSetting(dot_size=10))

        expected_attrs: Dict[str, Any] = {
            '_fill_color': '',
            '_fill_alpha': 1.0,
            '_line_color': '',
            '_line_thickness': 1,
            '_line_alpha': 1.0,
            '_current_line': None,
            '_line_cap': ap.LineCaps.BUTT.value,
            '_line_joints': ap.LineJoints.MITER.value,
            '_line_dot_setting': None,
            '_line_dash_setting': None,
            '_line_round_dot_setting': None,
            '_line_dash_dot_setting': None,
        }
        sprite.graphics.clear()
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs,
            any_obj=sprite.graphics)
        assert sprite.graphics.num_children == 0
