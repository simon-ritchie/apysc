import apysc as ap
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialSearchIcon:
    @apply_test_settings()
    def test___init__(self) -> None:
        icon: ap.material_icons.MaterialSearchIcon = (
            ap.material_icons.MaterialSearchIcon(
                fill_color=ap.Colors.WHITE_FFFFFF,
                fill_alpha=0.5,
                x=100,
                y=150,
                width=40,
                height=50,
                variable_name_suffix="test_suffix",
            )
        )
        assert icon._fill_color == ap.Colors.WHITE_FFFFFF
        assert icon._fill_alpha._value == 0.5
        assert icon._x._value == 100
        assert icon._y._value == 150
        assert icon._width._value == 40
        assert icon._height._value == 50
        assert var_names.MATERIAL_SEARCH_ICON in icon.variable_name
        assert "test_suffix" in icon._variable_name_suffix
