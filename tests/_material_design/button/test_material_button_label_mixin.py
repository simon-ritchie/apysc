import apysc as ap
from apysc._expression import expression_data_util
from apysc._material_design.button.material_button_const import ICON_INNER_PADDING_WIDTH, ICON_OUTER_PADDING_WIDTH, ICON_SIZE, NO_ICON_OUTER_PADDING
from apysc._material_design.icon.material_home_icon import MaterialHomeIcon
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialButtonLabelMixIn:
    @apply_test_settings()
    def test__initialize_label(self) -> None:
        button: ap.MaterialFilledButton = ap.MaterialFilledButton(
            label="Test button",
            text_color=ap.Colors.RED_BROWN_622F22,
            font_family=["Arial", "Helvetica"],
            font_size=20,
            variable_name_suffix="test_button",
        )
        assert button._label == ap.String("Test button")
        assert isinstance(button._label_text, ap.SvgText)
        assert button._label_text.parent == button
        assert button._text_color == ap.Colors.RED_BROWN_622F22
        assert button._font_family == ap.Array(["Arial", "Helvetica"])
        assert button._font_size == ap.Int(20)

    @apply_test_settings()
    def test__locate_label_text(self) -> None:
        button: ap.MaterialFilledButton = ap.MaterialFilledButton(
            label="Test button",
            variable_name_suffix="test_button",
        )
        assert button._label_text.x == ap.Number(NO_ICON_OUTER_PADDING)
        assert button._label_text.y != ap.Number(0)
        assert isinstance(button._label_text.y, ap.Number)
        expression: str = expression_data_util.get_current_expression()
        assert "material_button_label_text_x" in expression
        assert "material_button_label_text_y" in expression

        button = ap.MaterialFilledButton(
            label="Test button",
            prefix_icon=MaterialHomeIcon(),
            variable_name_suffix="test_button",
        )
        assert button._label_text.x == ap.Number(
            ICON_OUTER_PADDING_WIDTH + ICON_SIZE + ICON_INNER_PADDING_WIDTH,
        )
