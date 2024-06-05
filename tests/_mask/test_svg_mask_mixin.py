import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test_svg_mask() -> None:
    mask: ap.SvgMask = ap.SvgMask()
    rectangle: ap.Rectangle = ap.Rectangle(x=50, y=50, width=100, height=100)
    assert rectangle.svg_mask is None

    rectangle.svg_mask = None
    expression: str = expression_data_util.get_current_expression()
    expected: str = f"{rectangle.variable_name}.unclip();"
    assert expected in expression
    assert rectangle.svg_mask is None

    rectangle.svg_mask = mask
    expression = expression_data_util.get_current_expression()
    expected = f"{rectangle.variable_name}.clipWith({mask.variable_name});"
    assert expected in expression
    assert rectangle.svg_mask == mask
