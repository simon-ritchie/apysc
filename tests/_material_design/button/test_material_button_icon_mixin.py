from apysc._expression import expression_data_util
from apysc._material_design.button.material_button_const import ICON_SIZE
from apysc._material_design.button.material_button_icon_mixin import MaterialButtonIconMixIn
from apysc._testing.testing_helper import apply_test_settings
import apysc as ap
from apysc._material_design.icon.material_home_icon import MaterialHomeIcon
from apysc._material_design.icon.material_add_box_icon import MaterialAddBoxIcon


class TestMaterialButtonIconMixIn:
    @apply_test_settings()
    def test__locate_icons(self) -> None:
        prefix_icon: MaterialHomeIcon = MaterialHomeIcon()
        suffix_icon: MaterialAddBoxIcon = MaterialAddBoxIcon()
        ap.MaterialFilledButton(
            label="Test button",
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon,
            variable_name_suffix="test_button"
        )
        expression: str = expression_data_util.get_current_expression()
        assert "prefix_icon_x" in expression
        assert "prefix_icon_y" in expression
        assert "suffix_icon_x" in expression
        assert "suffix_icon_y" in expression
        assert prefix_icon.x != 0
        assert prefix_icon.y != 0
        assert suffix_icon.x != 0
        assert suffix_icon.y != 0

    @apply_test_settings()
    def test__add_icons(self) -> None:
        prefix_icon: MaterialHomeIcon = MaterialHomeIcon()
        suffix_icon: MaterialAddBoxIcon = MaterialAddBoxIcon()
        button: ap.MaterialFilledButton = ap.MaterialFilledButton(
            label="Test button",
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon,
            variable_name_suffix="test_button"
        )
        assert prefix_icon.parent == button
        assert suffix_icon.parent == button

    @apply_test_settings()
    def test__resize_icon_size(self) -> None:
        prefix_icon: MaterialHomeIcon = MaterialHomeIcon()
        suffix_icon: MaterialAddBoxIcon = MaterialAddBoxIcon()
        ap.MaterialFilledButton(
            label="Test button",
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon,
            variable_name_suffix="test_button"
        )
        expression: str = expression_data_util.get_current_expression()
        assert "prefix_icon_width" in expression
        assert "prefix_icon_height" in expression
        assert "suffix_icon_width" in expression
        assert "suffix_icon_height" in expression
        assert prefix_icon.width == ap.Int(ICON_SIZE)
        assert prefix_icon.height == ap.Int(ICON_SIZE)
        assert suffix_icon.width == ap.Int(ICON_SIZE)
        assert suffix_icon.height == ap.Int(ICON_SIZE)

    @apply_test_settings()
    def test__set_fill_color_to_icons(self) -> None:
        prefix_icon: MaterialHomeIcon = MaterialHomeIcon()
        suffix_icon: MaterialAddBoxIcon = MaterialAddBoxIcon()
        button: ap.MaterialFilledButton = ap.MaterialFilledButton(
            label="Test button",
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon,
        )
        button._set_fill_color_to_icons(
            color=ap.Colors.RED_BROWN_622F22,
            prefix_icon=prefix_icon,
            suffix_icon=suffix_icon
        )
        assert prefix_icon.fill_color == ap.Colors.RED_BROWN_622F22
        assert suffix_icon.fill_color == ap.Colors.RED_BROWN_622F22
