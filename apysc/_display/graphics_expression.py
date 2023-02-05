"""Graphics class-related expression implementations.
"""

from apysc._html.debug_mode import add_debug_info_setting
from apysc._type.int import Int
from apysc._type.number import Number
from apysc._type.string import String


@add_debug_info_setting(module_name=__name__)
def append_fill_expression(
    *, fill_color: String, expression: str, indent_num: int
) -> str:
    """
    Append a fill expression to specified expression's string.

    Parameters
    ----------
    fill_color : String
        A fill-color to use.
    expression : str
        Expression string to be appended fill expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    from apysc._string import indent_util

    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    if fill_color._value == "":
        expression += f'\n{spaces}fill: "none",'
        return expression
    expression += f"\n{spaces}fill: {fill_color.variable_name},"
    return expression


@add_debug_info_setting(module_name=__name__)
def append_fill_opacity_expression(
    *, fill_alpha: Number, expression: str, indent_num: int
) -> str:
    """
    Append a fill opacity expression to a specified expression's string.

    Parameters
    ----------
    fill_alpha : Number
        A fill-alpha to use.
    expression : str
        Expression string to be appended fill opacity expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    from apysc._string import indent_util

    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f'\n{spaces}"fill-opacity": {fill_alpha.variable_name},'
    return expression


@add_debug_info_setting(module_name=__name__)
def append_x_expression(*, x: Number, expression: str, indent_num: int) -> str:
    """
    Append x position expression to specified expression's string.

    Parameters
    ----------
    x : Number
        An x-coordinate to use.
    expression : str
        Expression string to be appended x position expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    from apysc._string import indent_util

    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f"\n{spaces}x: {x.variable_name},"
    return expression


@add_debug_info_setting(module_name=__name__)
def append_y_expression(*, y: Number, expression: str, indent_num: int) -> str:
    """
    Append y position expression to specified expression's string.

    Parameters
    ----------
    y : Number
        A y-coordinate to use.
    expression : str
        Expression string to be appended y position expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    from apysc._string import indent_util

    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f"\n{spaces}y: {y.variable_name},"
    return expression


@add_debug_info_setting(module_name=__name__)
def append_stroke_expression(
    *, line_color: String, expression: str, indent_num: int
) -> str:
    """
    Append stroke expression to specified expression's string.

    Parameters
    ----------
    line_color : String
        A line-color to use.
    expression : str
        Expression string to be appended stroke expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    from apysc._string import indent_util

    if line_color._value == "":
        return expression
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f"\n{spaces}stroke: {line_color.variable_name},"
    return expression


@add_debug_info_setting(module_name=__name__)
def append_stroke_width_expression(
    *, line_thickness: Int, expression: str, indent_num: int
) -> str:
    """
    Append stroke width expression to specified expression's string.

    Parameters
    ----------
    line_thickness : Int
        A line-thickness to use.
    expression : str
        Expression string to be appended stroke width expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    from apysc._string import indent_util

    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f'\n{spaces}"stroke-width": ' f"{line_thickness.variable_name},"
    return expression


@add_debug_info_setting(module_name=__name__)
def append_stroke_opacity_expression(
    *, line_alpha: Number, expression: str, indent_num: int
) -> str:
    """
    Append stroke opacity expression to specified expression's string.

    Parameters
    ----------
    line_alpha : Number
        A line-alpha to use.
    expression : str
        Expression string to be appended stroke opacity expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    from apysc._string import indent_util

    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f'\n{spaces}"stroke-opacity": {line_alpha.variable_name},'
    return expression


@add_debug_info_setting(module_name=__name__)
def append_stroke_linecap_expression(
    *, line_cap: String, expression: str, indent_num: int
) -> str:
    """
    Append stroke line cap expression to specified expression's string.

    Parameters
    ----------
    line_cap : String
        A line-cap to use.
    expression : str
        Expression string to be appended stroke linecap expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    import apysc as ap
    from apysc._string import indent_util

    if line_cap._value == ap.LineCaps.BUTT.value:
        return expression
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f'\n{spaces}"stroke-linecap": {line_cap.variable_name},'
    return expression


@add_debug_info_setting(module_name=__name__)
def append_stroke_linejoin_expression(
    *, line_joints: String, expression: str, indent_num: int
) -> str:
    """
    Append stroke line-join expression to specified
    expression's string.

    Parameters
    ----------
    line_joints : String
        A line-join to use.
    expression : str
        Expression string to be appended stroke linejoin expression.
    indent_num : int
        Indentation number.

    Returns
    -------
    expression : str
        After appended expression string.
    """
    import apysc as ap
    from apysc._string import indent_util

    if line_joints._value == ap.LineJoints.MITER.value:
        return expression
    spaces: str = indent_util.make_spaces_for_html(indent_num=indent_num)
    expression += f'\n{spaces}"stroke-linejoin": ' f"{line_joints.variable_name},"
    return expression
