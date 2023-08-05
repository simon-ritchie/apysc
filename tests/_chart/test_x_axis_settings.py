import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestXAxisSettings:
    @apply_test_settings()
    def test___init__(self) -> None:
        setting: ap.XAxisSettings = ap.XAxisSettings(
            x_axis_column_name="test_column",
            tick_max_num=10,
            tick_text_font_size=15,
            tick_text_font_family=["Arial"],
            tick_text_fill_color=ap.Color("#0af"),
            tick_text_fill_alpha=0.5,
            tick_text_bold=True,
            tick_text_italic=True,
            line_color=ap.Color("#666"),
            line_thickness=3,
            line_alpha=0.3,
            is_display_axis_label=False,
            axis_label_position=ap.XAxisLabelPosition.OUTER_LEFT,
            axis_label_font_size=20,
            axis_label_font_family=["Impact"],
            axis_label_fill_color=ap.Color("#333"),
            axis_label_fill_alpha=0.7,
            axis_label_bold=False,
            axis_label_italic=False,
            variable_name_suffix="test_suffix",
        )
        assert setting._x_axis_column_name == ap.String("test_column")
        assert setting._tick_max_num == ap.Int(10)
        if setting._tick_max_num is not None:
            assert setting._tick_max_num._variable_name_suffix == "test_suffix"
        assert setting._tick_text_font_size == ap.Int(15)
        assert setting._tick_text_font_family == ap.Array([ap.String("Arial")])
        assert setting._tick_text_fill_color == ap.Color("#00aaff")
        assert setting._tick_text_fill_alpha == ap.Number(0.5)
        assert setting._tick_text_bold == ap.Boolean(True)
        assert setting._tick_text_italic == ap.Boolean(True)
        assert setting._line_color == ap.Color("#666666")
        assert setting._line_thickness == ap.Int(3)
        assert setting._line_alpha == ap.Number(0.3)
        assert setting._is_display_axis_label == ap.Boolean(False)
        assert setting._x_axis_label_position == ap.XAxisLabelPosition.OUTER_LEFT
        assert setting._axis_label_font_size == ap.Int(20)
        assert setting._axis_label_font_family == ap.Array([ap.String("Impact")])
        assert setting._axis_label_fill_color == ap.Color("#333333")
        assert setting._axis_label_fill_alpha == ap.Number(0.7)
        assert setting._axis_label_bold == ap.Boolean(False)
        assert setting._axis_label_italic == ap.Boolean(False)
