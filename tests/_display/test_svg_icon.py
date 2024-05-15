import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._expression import var_names


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
