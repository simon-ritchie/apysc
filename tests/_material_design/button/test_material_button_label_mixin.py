import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestMaterialButtonLabelMixIn:
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
