"""Graphics class related expression implementations.
"""

from apyscript.display.graphics import Graphics
from apyscript.display.graphic_base import GraphicBase


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
    spaces: str = ' ' * (indent_num * 2)
    expression += (
        f'\n{spaces}fill: "{graphics.fill_color}",'
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
    spaces: str = ' ' * (indent_num * 2)
    expression += (
        f'\n{spaces}x: {graphic.x},'
    )
    return expression
