import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression import expression_data_util, var_names


class TestSvgIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        svg_icon: ap.SvgIcon = ap.SvgIcon(
            svg_icon_html="<svg>...</svg>",
            parent=sprite,
            variable_name_suffix="test_suffix",
        )
        assert svg_icon._svg_icon_html == "<svg>...</svg>"
        assert svg_icon._variable_name_suffix == "test_suffix"
        assert svg_icon.parent == sprite
        assert var_names.SVG_ICON in svg_icon.variable_name

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        svg_icon: ap.SvgIcon = ap.SvgIcon(svg_icon_html="<svg>...</svg>",)
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"var {svg_icon.variable_name} = "
            f"SVG('<svg>...</svg>');"
        )
        assert expected in expression