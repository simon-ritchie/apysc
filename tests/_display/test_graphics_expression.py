import re
from typing import Match
from typing import Optional

import apysc as ap
from apysc._display import graphics_expression
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_append_fill_expression() -> None:
    fill_color: ap.String = ap.String("")
    expression: str = ".attr({"
    expression = graphics_expression.append_fill_expression(
        fill_color=fill_color, expression=expression, indent_num=1
    )
    assert expression == '.attr({\n  fill: "none",'

    fill_color.value = ap.String("#333")
    expression = ".attr({"
    expression = graphics_expression.append_fill_expression(
        fill_color=fill_color, expression=expression, indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf"\n  fill: {fill_color.variable_name},"),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_x_expression() -> None:
    expression: str = ".attr({"
    x: ap.Int = ap.Int(100)
    expression = graphics_expression.append_x_expression(
        x=x, expression=expression, indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf"\n  x: {x.variable_name},"),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_y_expression() -> None:
    y: ap.Int = ap.Int(200)
    expression: str = ".attr({"
    expression = graphics_expression.append_y_expression(
        y=y, expression=expression, indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf"\n  y: {y.variable_name},"),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_fill_opacity_expression() -> None:
    fill_alpha: ap.Number = ap.Number(0.5)
    expression: str = ".attr({"
    expression = graphics_expression.append_fill_opacity_expression(
        fill_alpha=fill_alpha, expression=expression, indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf'\n  "fill-opacity": {fill_alpha.variable_name},'),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_stroke_expression() -> None:
    line_color: ap.String = ap.String("")
    expression: str = ".attr({"
    expression = graphics_expression.append_stroke_expression(
        line_color=line_color, expression=expression, indent_num=1
    )
    assert expression == ".attr({"

    line_color.value = ap.String("#666")
    expression = graphics_expression.append_stroke_expression(
        line_color=line_color, expression=expression, indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf"\n  stroke: {line_color.variable_name},"),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_stroke_width_expression() -> None:
    line_thickness: ap.Int = ap.Int(3)
    expression: str = ".attr({"
    expression = graphics_expression.append_stroke_width_expression(
        line_thickness=line_thickness, expression=expression, indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf'\n  "stroke-width": {line_thickness.variable_name},'),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_stroke_opacity_expression() -> None:
    line_alpha: ap.Number = ap.Number(0.25)
    expression: str = ".attr({"
    expression = graphics_expression.append_stroke_opacity_expression(
        line_alpha=line_alpha, expression=expression, indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf'\n  "stroke-opacity": {line_alpha.variable_name},'),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_stroke_linecap_expression() -> None:
    line_cap: ap.String = ap.String(ap.LineCaps.BUTT.value)
    expression: str = graphics_expression.append_stroke_linecap_expression(
        line_cap=line_cap, expression=".attr({", indent_num=1
    )
    assert expression == ".attr({"

    line_cap = ap.String(ap.LineCaps.ROUND.value)
    expression = graphics_expression.append_stroke_linecap_expression(
        line_cap=line_cap, expression=".attr({", indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r".attr\(\{" rf'\n  "stroke-linecap": {line_cap.variable_name},'),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


@apply_test_settings()
def test_append_stroke_linejoin_expression() -> None:
    expression: str = graphics_expression.append_stroke_linejoin_expression(
        line_joints=ap.String(ap.LineJoints.MITER.value),
        expression=".attr({",
        indent_num=1,
    )
    assert expression == ".attr({"

    line_joints: ap.String = ap.String(ap.LineJoints.BEVEL.value)
    expression = graphics_expression.append_stroke_linejoin_expression(
        line_joints=line_joints, expression=".attr({", indent_num=1
    )
    match: Optional[Match] = re.search(
        pattern=(r"\.attr\(\{" rf'\n  "stroke-linejoin": {var_names.STRING}.+,'),
        string=expression,
        flags=re.MULTILINE,
    )
    assert match is not None


def assert_fill_attr_expression_exists(expression: str) -> None:
    """
    Assert fill attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert "fill: " in expression


def assert_fill_opacity_attr_expression_exists(expression: str) -> None:
    """
    Assert fill opacity attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert '"fill-opacity": ' in expression


def assert_x_attr_expression_exists(expression: str) -> None:
    """
    Assert x attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert "x: " in expression


def assert_y_attr_expression_exists(expression: str) -> None:
    """
    Assert y attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert "y: " in expression


def assert_stroke_attr_expression_exists(expression: str) -> None:
    """
    Assert stroke attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert "stroke: " in expression


def assert_stroke_width_attr_expression_exists(expression: str) -> None:
    """
    Assert stroke width attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert '"stroke-width": ' in expression


def assert_stroke_opacity_attr_expression_exists(expression: str) -> None:
    """
    Assert stroke opacity attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert '"stroke-opacity": ' in expression


def assert_stroke_linecap_attr_expression_exists(expression: str) -> None:
    """
    Assert storoke linecap attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert '"stroke-linecap": ' in expression


def assert_stroke_linejoin_attr_expression_exists(expression: str) -> None:
    """
    Assert stroke linejoin attribute's expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target attribute's expression not exists.
    """
    assert '"stroke-linejoin": ' in expression


def assert_stroke_dasharray_css_expression_exists(expression: str) -> None:
    """
    Assert stroke dasharray css expression exists in specified one.

    Parameters
    ----------
    expression : str
        Target expression to check.

    Raises
    ------
    AssertionError
        If target css expression not exists.
    """
    assert '.css("stroke-dasharray", ' in expression
