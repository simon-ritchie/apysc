"""Definition of callable's acceptable arguments.
"""


from typing import List, Type


def get_acceptable_arg_types() -> List[Type]:
    """
    Get expression callable's acceptable argument types.

    Notes
    -----
    To avoid recursive import, each modules are imported in
    this function (not on top-level scope).

    Returns
    -------
    arg_types : list of type
        Acceptable argument types.
    """
    from apyscript.display.stage import Stage
    from apyscript.display.sprite import DisplayObject
    from apyscript.display.graphics import Graphics
    from apyscript.display.graphic_base import GraphicBase
    arg_types: List[Type] = [
        Stage,
        DisplayObject,
        Graphics,
        GraphicBase,
    ]
    return arg_types
