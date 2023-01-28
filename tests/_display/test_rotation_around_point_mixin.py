import re
from random import randint
from typing import List
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display import rotation_interface_helper
from apysc._display.rotation_around_point_mixin import RotationAroundPointMixIn
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._type.expression_string import ExpressionString
from apysc._testing.testing_helper import apply_test_settings


class _TestMixIn(RotationAroundPointMixIn):
    def __init__(self) -> None:
        """
        The class for the testing.
        """
        self.variable_name = "test_rotation_around_point_mixin"


class TestRotationAroundPointMixIn:
    @apply_test_settings()
    def test__initialize_rotation_around_point_if_not_initialized(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        mixin._initialize_rotation_around_point_if_not_initialized()
        assert mixin._rotation_around_point == {}

        mixin._rotation_around_point["a"] = ap.Int(10)
        mixin._initialize_rotation_around_point_if_not_initialized()
        assert mixin._rotation_around_point == {"a": ap.Int(10)}

    @apply_test_settings()
    def test_get_rotation_around_point(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        rotation: ap.Int = mixin.get_rotation_around_point(x=x, y=y)
        assert rotation == 0

        key_exp_str: ExpressionString = (
            rotation_interface_helper.get_coordinates_key_for_expression(x=100, y=200)
        )
        mixin._rotation_around_point[key_exp_str.value] = ap.Int(50)
        rotation = mixin.get_rotation_around_point(x=x, y=y)
        assert rotation == 50

    @apply_test_settings()
    def test_set_rotation_around_point(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        rotation: ap.Int = ap.Int(50)
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        mixin.set_rotation_around_point(rotation=rotation, x=x, y=y)
        rotation = mixin.get_rotation_around_point(x=x, y=y)
        assert rotation == 50

    @apply_test_settings()
    def test__append_rotation_around_point_update_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        rotation: ap.Int = ap.Int(50)
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)
        mixin.set_rotation_around_point(rotation=rotation, x=x, y=y)
        expression: str = expression_data_util.get_current_expression()
        assert ".rotate(" in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        x: ap.Int = ap.Int(50)
        y: ap.Int = ap.Int(100)
        rotation: ap.Int = ap.Int(90)
        mixin.set_rotation_around_point(rotation=rotation, x=x, y=y)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        key_exp_str: ExpressionString = (
            rotation_interface_helper.get_coordinates_key_for_expression(
                x=int(x._value), y=int(y._value)
            )
        )
        assert mixin._rotation_around_point_snapshots == {
            snapshot_name: {key_exp_str.value: rotation}
        }

        mixin.set_rotation_around_point(rotation=ap.Int(120), x=x, y=y)
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert mixin._rotation_around_point_snapshots == {
            snapshot_name: {key_exp_str.value: rotation}
        }

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: _TestMixIn = _TestMixIn()
        x: ap.Int = ap.Int(50)
        y: ap.Int = ap.Int(100)
        mixin.set_rotation_around_point(rotation=ap.Int(90), x=x, y=y)
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin.set_rotation_around_point(rotation=ap.Int(120), x=x, y=y)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        key_exp_str: ExpressionString = (
            rotation_interface_helper.get_coordinates_key_for_expression(
                x=int(x._value), y=int(y._value)
            )
        )
        assert mixin._rotation_around_point[key_exp_str.value] == 90

        mixin.set_rotation_around_point(rotation=ap.Int(120), x=x, y=y)
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._rotation_around_point[key_exp_str.value] == 120

    @apply_test_settings()
    def test__get_rotation_around_point_updating_expression(self) -> None:
        expression_data_util.empty_expression()
        mixin: _TestMixIn = _TestMixIn()
        rotation: ap.Int = ap.Int(50)
        x: ap.Int = ap.Int(100)
        y: ap.Int = ap.Int(200)

        key_exp_str: ExpressionString = (
            rotation_interface_helper.get_coordinates_key_for_expression(x=x, y=y)
        )
        key_exp_value: str = key_exp_str.value
        key_exp_value = key_exp_value.replace("(", "\\(")
        key_exp_value = key_exp_value.replace(")", "\\)")
        key_exp_value = key_exp_value.replace("+", "\\+")
        expression: str = mixin._get_rotation_around_point_updating_expression(
            rotation=rotation, x=x, y=y
        )
        patterns: List[str] = [
            rf"if \({key_exp_value} in "
            rf"{mixin._rotation_around_point.variable_name}\) {{",
            rf"\n  var {var_names.INT}_.+? = "
            rf"{mixin._rotation_around_point.variable_name}\["
            rf"{key_exp_value}\];",
            r"\n}else {" rf"\n  {var_names.INT}_.+? = 0;",
            r"\n}",
            rf"\n{mixin.variable_name}\.rotate\("
            rf"-{var_names.INT}_.+?, {x.variable_name}, {y.variable_name}\);",
            rf"\n{mixin.variable_name}\.rotate\("
            rf"{rotation.variable_name}, {x.variable_name}, "
            rf"{y.variable_name}\);",
            rf"\n{mixin._rotation_around_point.variable_name}\["
            rf"{key_exp_value}\] = {rotation.variable_name};",
        ]
        for i, pattern in enumerate(patterns):
            match: Optional[Match] = re.search(
                pattern=pattern, string=expression, flags=re.MULTILINE | re.DOTALL
            )
            assert match is not None, f"index: {i}, \n{expression}\n\n{pattern}"
