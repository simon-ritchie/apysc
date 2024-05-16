import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestSvgIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        svg_icon: ap.SvgIcon = ap.SvgIcon(
            svg_icon_html="<svg>...</svg>",
            x=50,
            y=100,
            width=48,
            fill_color=ap.Colors.GRAY_777777,
            fill_alpha=0.5,
            parent=sprite,
            variable_name_suffix="test_suffix",
        )
        assert svg_icon._svg_icon_html == "<svg>...</svg>"
        assert svg_icon.x == ap.Number(50)
        assert svg_icon.y == ap.Number(100)
        assert svg_icon.fill_color == ap.Colors.GRAY_777777
        assert svg_icon.fill_alpha == ap.Number(0.5)
        assert svg_icon._variable_name_suffix == "test_suffix"
        assert svg_icon.parent == sprite
        assert var_names.SVG_ICON in svg_icon.variable_name

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        svg_icon: ap.SvgIcon = ap.SvgIcon(
            svg_icon_html="<svg>...</svg>",
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = f"var {svg_icon.variable_name} = " f"SVG('<svg>...</svg>');"
        assert expected in expression
