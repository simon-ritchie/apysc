import re
from typing import List
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display import scale_interface_helper
from apysc._testing.testing_helper import apply_test_settings
from apysc._type.expression_string import ExpressionString


@apply_test_settings()
def test_get_coordinate_key_for_expression() -> None:
    key_exp_str: ExpressionString = (
        scale_interface_helper.get_coordinate_key_for_expression(coordinate=10)
    )
    assert key_exp_str.value == "String(10.000)"

    x: ap.Number = ap.Number(10)
    key_exp_str = scale_interface_helper.get_coordinate_key_for_expression(coordinate=x)
    expected: str = f"String({x.variable_name})"
    assert key_exp_str.value == expected


@apply_test_settings()
def test_get_scale_updating_expression() -> None:
    coordinate: ap.Number = ap.Number(100)
    key_exp_str: ExpressionString = (
        scale_interface_helper.get_coordinate_key_for_expression(
            coordinate=float(coordinate._value)
        )
    )
    scale_val: ap.Number = ap.Number(0.5)
    scale_dict: ap.Dictionary = ap.Dictionary({key_exp_str.value: scale_val})
    expression: str = scale_interface_helper.get_scale_updating_expression(
        coordinate=coordinate,
        scale_dict=scale_dict,
        interface_variable_name="test_interface",
        coordinate_type=scale_interface_helper.CoordinateType.X,
    )
    expression_lines: List[str] = expression.splitlines()
    patterns: List[str] = [
        rf"if \(.+? in {scale_dict.variable_name}\) {{",
        rf"  var .+? = {scale_dict.variable_name}\[.+?\];",
        r"}else {",
        r"  .+? = 1\.0;",
        r"}",
        rf"test_interface.scale\(1 / .+?, 1, " rf"{coordinate.variable_name}, 0\);",
        rf"test_interface.scale\({scale_val.variable_name}, 1, "
        rf"{coordinate.variable_name}, 0\);",
        rf"{scale_dict.variable_name}\[.+?\] = {scale_val.variable_name};",
    ]
    for expression, pattern in zip(expression_lines, patterns):
        match: Optional[Match] = re.search(pattern=pattern, string=expression)
        assert match is not None, f"expression: {expression}\npattern: {pattern}"

    expression = scale_interface_helper.get_scale_updating_expression(
        coordinate=coordinate,
        scale_dict=scale_dict,
        interface_variable_name="test_interface",
        coordinate_type=scale_interface_helper.CoordinateType.Y,
    )
    patterns = [
        rf"test_interface.scale\(1, 1 / .+?, " rf"0, {coordinate.variable_name}\);",
        rf"test_interface.scale\(1, {scale_val.variable_name}, "
        rf"0, {coordinate.variable_name}\);",
    ]
    for pattern in patterns:
        match = re.search(pattern=pattern, string=expression, flags=re.MULTILINE)
        assert match is not None, f"expression: {expression}\npattern: {pattern}"
