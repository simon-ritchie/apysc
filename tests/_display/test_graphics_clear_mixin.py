from typing import Any
from typing import Dict

import apysc as ap
from apysc._testing import testing_helper
from apysc._testing.testing_helper import apply_test_settings


class TestGraphicsClearMixIn:
    @apply_test_settings()
    def test_clear(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        sprite.graphics.begin_fill(color=ap.Color("#000"))
        sprite.graphics.line_style(
            color=ap.Color("#aaa"),
            cap=ap.LineCaps.ROUND,
            joints=ap.LineJoints.BEVEL,
            dot_setting=ap.LineDotSetting(dot_size=10),
        )

        expected_attrs: Dict[str, Any] = {
            "_fill_color": ap.COLORLESS,
            "_fill_alpha": 1.0,
            "_line_color": ap.COLORLESS,
            "_line_thickness": 1,
            "_line_alpha": 1.0,
            "_current_line": None,
            "_line_cap": ap.LineCaps.BUTT.value,
            "_line_joints": ap.LineJoints.MITER.value,
            "_line_dot_setting": None,
            "_line_dash_setting": None,
            "_line_round_dot_setting": None,
            "_line_dash_dot_setting": None,
        }
        sprite.graphics.clear()
        testing_helper.assert_attrs(
            expected_attrs=expected_attrs, any_obj=sprite.graphics
        )
        assert sprite.graphics.num_children == 0
