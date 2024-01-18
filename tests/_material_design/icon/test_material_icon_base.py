import apysc as ap
from apysc._expression import expression_data_util
from apysc._expression import var_names
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialIconBase:
    @apply_test_settings()
    def test__make_variable_name_if_empty(self) -> None:
        icon: ap.MaterialIconBase = ap.MaterialIconBase(
            svg_path_value="",
            fill_color=ap.Colors.WHITE_FFFFFF,
            variable_name="",
        )
        assert icon.variable_name.startswith(var_names.MATERIAL_ICON)

        icon = ap.MaterialIconBase(
            svg_path_value="",
            fill_color=ap.Colors.WHITE_FFFFFF,
            variable_name="test_icon",
        )
        assert icon.variable_name == "test_icon"

    @apply_test_settings()
    def test___repr__(self) -> None:
        icon: ap.MaterialIconBase = ap.MaterialIconBase(
            svg_path_value="abc",
            fill_color=ap.Colors.WHITE_FFFFFF,
            variable_name="test_icon",
        )
        repr_str: str = repr(icon)
        assert repr_str == 'MaterialIconBase("abc")'

    @apply_test_settings()
    def test__initialize_with_base_value(self) -> None:
        icon: ap.MaterialIconBase = ap.MaterialIconBase._initialize_with_base_value()
        assert icon._svg_path_value == ""

    @apply_test_settings()
    def test__append_constructor_expression(self) -> None:
        stage: ap.Stage = ap.get_stage()
        icon: ap.MaterialIconBase = ap.MaterialIconBase(
            svg_path_value="abc",
            fill_color=ap.Colors.WHITE_FFFFFF,
            variable_name="test_icon",
        )
        expression: str = expression_data_util.get_current_expression()
        expected: str = (
            f"{icon.variable_name} = "
            f"{stage.variable_name}.path({icon._svg_path_value.variable_name});"
        )
        assert expected in expression

    @apply_test_settings()
    def test___init__(self) -> None:
        sprite: ap.Sprite = ap.Sprite()
        icon: ap.MaterialIconBase = ap.MaterialIconBase(
            svg_path_value="abc",
            fill_color=ap.Colors.WHITE_FFFFFF,
            fill_alpha=0.5,
            width=100,
            height=150,
            x=200,
            y=300,
            parent=sprite,
            variable_name="test_icon",
            variable_name_suffix="test_suffix",
        )
        assert icon._svg_path_value._value == "abc"
        assert icon._fill_color == ap.Colors.WHITE_FFFFFF
        assert icon._fill_alpha._value == 0.5
        assert icon._width._value == 100
        assert icon._height._value == 150
        assert icon._x._value == 200
        assert icon._y._value == 300
        assert icon.parent == sprite
        assert "test_icon" in icon.variable_name
        assert "test_suffix" in icon.variable_name