"""Graphics class related expression implementations.
"""

from apyscript.display.graphics import Graphics


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
