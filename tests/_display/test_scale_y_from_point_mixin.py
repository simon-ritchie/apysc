import re
from random import randint
from typing import Dict
from typing import List
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display import scale_interface_helper
from apysc._display.scale_y_from_point_mixin import ScaleYFromPointMixIn
from apysc._expression import expression_data_util
from apysc._type.expression_string import ExpressionString
from apysc._testing.testing_helper import apply_test_settings


class _TestMixIn(ScaleYFromPointMixIn):
    def __init__(self) -> None:
        """
        Class for the testing of the `ScaleYFromPointMixIn` class.
        """
        self.variable_name = "test_scale_y_from_point_interface"


class TestScaleYFromPointMixIn:
    @apply_test_settings()
    def test__initialize_scale_y_from_point_if_not_initialized(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface._initialize_scale_y_from_point_if_not_initialized()
        assert interface._scale_y_from_point == {}

        interface._scale_y_from_point["a"] = ap.Number(10)
        interface._initialize_scale_y_from_point_if_not_initialized()
        assert interface._scale_y_from_point == {"a": ap.Number(10)}

    @apply_test_settings()
    def test_get_scale_y_from_point(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        scale_y: ap.Number = interface.get_scale_y_from_point(y=ap.Int(10))
        assert scale_y == 1.0

        key_exp_str: ExpressionString = (
            scale_interface_helper.get_coordinate_key_for_expression(coordinate=10)
        )
        interface._scale_y_from_point[key_exp_str] = ap.Number(0.5)
        scale_y = interface.get_scale_y_from_point(y=ap.Int(10))
        assert scale_y == 0.5

    @apply_test_settings()
    def test_set_scale_y_from_point(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.set_scale_y_from_point(scale_y=ap.Number(0.5), y=ap.Int(100))
        scale_y: ap.Number = interface.get_scale_y_from_point(y=ap.Int(100))
        assert scale_y == 0.5

    @apply_test_settings()
    def test__append_scale_y_from_point_update_expression(self) -> None:
        expression_data_util.empty_expression()
        interface: _TestMixIn = _TestMixIn()
        scale_y: ap.Number = ap.Number(0.5)
        y: ap.Int = ap.Int(100)
        interface.set_scale_y_from_point(scale_y=scale_y, y=y)
        expression: str = expression_data_util.get_current_expression()
        patterns: List[str] = [
            rf"{interface.variable_name}"
            rf"\.scale\(1, 1 / .+?, 0, {y.variable_name}\);",
            rf"{interface.variable_name}"
            rf".scale\(1, {scale_y.variable_name}, 0, {y.variable_name}\);",
        ]
        for pattern in patterns:
            match: Optional[Match] = re.search(
                pattern=pattern, string=expression, flags=re.MULTILINE
            )
            assert match is not None, f"expression: {expression}\npattern: {pattern}"

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.set_scale_y_from_point(scale_y=ap.Number(0.5), y=ap.Int(100))
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)

        interface.set_scale_y_from_point(scale_y=ap.Number(0.3), y=ap.Int(100))
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.get_scale_y_from_point(y=ap.Int(100)) == 0.5

    @apply_test_settings()
    def test__revert(self) -> None:
        interface: _TestMixIn = _TestMixIn()
        interface.set_scale_y_from_point(scale_y=ap.Number(0.5), y=ap.Int(100))
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        pre_dict: Dict[str, ap.Number] = {**interface._scale_y_from_point._value}
        interface.set_scale_y_from_point(scale_y=ap.Number(0.3), y=ap.Int(100))
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._scale_y_from_point == pre_dict

        interface.set_scale_y_from_point(scale_y=ap.Number(0.3), y=ap.Int(100))
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._scale_y_from_point != pre_dict
