"""Graphics class related expression implementations.
"""

from apyscript.display.graphic_base import GraphicBase
from apyscript.display.graphics import Graphics
from apyscript.string import indent_util


def append_fill_expression(
        graphics: Graphics, expression: str, indent_num: int) -> str:
    """
    Append fill expression to specified expression's string.

    Parameters
    ----------
    graphics : Graphics
        Target Graphics instance.
    expression : str
        Expression string to be appended fill expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    if graphics.fill_color is None:
        return expression
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += (
        f'\n{spaces}fill: "{graphics.fill_color}",'
    )
    return expression


def append_fill_opacity_expression(
        graphics: Graphics, expression: str, indent_num: int) -> str:
    """
    Append fill opacity expression to specified expression's string.

    Parameters
    ----------
    graphics : Graphics
        Target Graphics instance.
    expression : str
        Expression string to be appended fill opacity expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += (
        f'\n{spaces}"fill-opacity": {graphics.fill_alpha},'
    )
    return expression


def append_x_expression(
        graphic: GraphicBase, expression: str, indent_num: int) -> str:
    """
    Append x position expression to specified expression's string.

    Parameters
    ----------
    graphic : GraphicBase
        Target graphic instance, for example, Rectangle.
    expression : str
        Expression string to be appended x position expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += (
        f'\n{spaces}x: {graphic.x},'
    )
    return expression


def append_y_expression(
        graphic: GraphicBase, expression: str, indent_num: int) -> str:
    """
    Append y position expression to specified expression's string.

    Parameters
    ----------
    graphic : GraphicBase
        Target graphic instance, for example, Rectangle.
    expression : str
        Expression string to be appended y position expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += (
        f'\n{spaces}y: {graphic.y},'
    )
    return expression


def append_stroke_expression(
        graphics: Graphics, expression: str, indent_num: int) -> str:
    """
    Append stroke expression to specified expression's string.

    Parameters
    ----------
    graphics : Graphics
        Target Graphics instance.
    expression : str
        Expression string to be appended stroke expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    if graphics.line_color is None:
        return expression
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += (
        f'\n{spaces}stroke: "{graphics.line_color}",'
    )
    return expression


def append_stroke_width_expression(
        graphics: Graphics, expression: str, indent_num: int) -> str:
    """
    Append stroke width expression to specified expression's string.

    Parameters
    ----------
    graphics : Graphics
        Target Graphics instance.
    expression : str
        Expression string to be appended stroke width expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += (
        f'\n{spaces}"stroke-width": {graphics.line_thickness},'
    )
    return expression


def append_stroke_opacity_expression(
        graphics: Graphics, expression: str, indent_num: int) -> str:
    """
    Append stroke opacity expression to specified expression's string.

    Parameters
    ----------
    graphics : Graphics
        Target Graphics instance.
    expression : str
        Expression string to be appended stroke opacity expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += (
        f'\n{spaces}"stroke-opacity": {graphics.line_alpha},'
    )
    return expression
