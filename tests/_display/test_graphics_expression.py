import re
from random import randint
from typing import Match
from typing import Optional

from retrying import retry

import apysc as ap
from apysc._display import graphics_expression
from apysc._display.graphics import Graphics
from apysc._expression import var_names


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_fill_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_fill_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({\n  fill: "none",'

    graphics.begin_fill(color='#333')
    expression = '.attr({'
    expression = graphics_expression.append_fill_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  fill: {var_names.STRING}.+?,'
        ),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_x_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    rectangle: ap.Rectangle = ap.Rectangle(
        parent=sprite.graphics,
        x=100, y=200, width=300, height=400)
    expression: str = '.attr({'
    expression = graphics_expression.append_x_expression(
        graphic=rectangle, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  x: {var_names.INT}.+?,'
        ),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_y_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    rectangle: ap.Rectangle = ap.Rectangle(
        parent=sprite.graphics,
        x=100, y=200, width=300, height=400)
    expression: str = '.attr({'
    expression = graphics_expression.append_y_expression(
        graphic=rectangle, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  y: {var_names.INT}.+?,'),
        string=expression, flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_fill_opacity_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    graphics.begin_fill(color='#333', alpha=0.5)
    expression = graphics_expression.append_fill_opacity_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  "fill-opacity": {var_names.NUMBER}.+?,'),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_stroke_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.line_style(color='#666')
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  stroke: {var_names.STRING}.+?,'
        ),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_stroke_width_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.line_style(color='#666', thickness=3)
    expression = graphics_expression.append_stroke_width_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  "stroke-width": {var_names.INT}.+?,'),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_stroke_opacity_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    graphics: Graphics = sprite.graphics
    expression: str = '.attr({'
    expression = graphics_expression.append_stroke_expression(
        graphics=graphics, expression=expression, indent_num=1)
    assert expression == '.attr({'

    graphics.line_style(color='#666', alpha=0.25)
    expression = graphics_expression.append_stroke_opacity_expression(
        graphics=graphics, expression=expression, indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  "stroke-opacity": {var_names.NUMBER}.+?,'),
        string=expression,
        flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_stroke_linecap_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    expression: str = graphics_expression.append_stroke_linecap_expression(
        graphics=sprite.graphics,
        expression='.attr({',
        indent_num=1)
    assert expression == '.attr({'

    sprite.graphics.line_style(color='#0af', cap=ap.LineCaps.ROUND)
    expression = graphics_expression.append_stroke_linecap_expression(
        graphics=sprite.graphics,
        expression='.attr({',
        indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'.attr\(\{'
            rf'\n  "stroke-linecap": {var_names.STRING}_.+,'
        ),
        string=expression, flags=re.MULTILINE)
    assert match is not None


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_append_stroke_linejoin_expression() -> None:
    stage: ap.Stage = ap.Stage()
    sprite: ap.Sprite = ap.Sprite(stage=stage)
    expression: str = graphics_expression.append_stroke_linejoin_expression(
        graphics=sprite.graphics,
        expression='.attr({',
        indent_num=1)
    assert expression == '.attr({'

    sprite.graphics.line_style(color='#0af', joints=ap.LineJoints.BEVEL)
    expression = graphics_expression.append_stroke_linejoin_expression(
        graphics=sprite.graphics,
        expression='.attr({',
        indent_num=1)
    match: Optional[Match] = re.search(
        pattern=(
            r'\.attr\(\{'
            rf'\n  "stroke-linejoin": {var_names.STRING}.+,'
        ),
        string=expression, flags=re.MULTILINE)
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
    assert 'fill: ' in expression


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
    assert 'x: ' in expression


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
    assert 'y: ' in expression


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
    assert 'stroke: ' in expression


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
