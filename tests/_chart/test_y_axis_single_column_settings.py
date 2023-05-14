import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestYAxisSingleColumnSettings:
    @apply_test_settings()
    def test___init__(self) -> None:
        setting: ap.YAxisSingleColumnSettings = ap.YAxisSingleColumnSettings(
            y_axis_column_name="test_column",
            y_min=0,
            tick_culling_max=20,
            tick_text_font_family=["Arial"],
            tick_text_fill_color="#666",
            tick_text_fill_alpha=0.5,
            tick_text_bold=True,
            tick_text_italic=True,
            line_color="#333",
            line_thickness=2,
            line_alpha=0.7,
            is_display_axis_label=False,
            axis_label_position=ap.YAxisLabelPosition.OUTER_BOTTOM,
            axis_label_font_size=15,
            axis_label_font_family=["Impact"],
            axis_label_fill_color="#777",
            axis_label_fill_alpha=0.9,
            axis_label_bold=True,
            axis_label_italic=True,
            top_margin=20,
            left_margin=30,
            variable_name_suffix="test_suffix",
        )
        assert setting._y_axis_column_name == ap.String("test_column")
        assert setting._y_min == ap.Number(0)
        assert setting._y_axis_column_name._variable_name_suffix == "test_suffix"
        assert setting._tick_culling_max == ap.Int(20)
        assert setting._tick_text_font_family == ap.Array([ap.String("Arial")])
        assert setting._tick_text_fill_color == ap.String("#666666")
        assert setting._tick_text_fill_alpha == ap.Number(0.5)
        assert setting._tick_text_bold == ap.Boolean(True)
        assert setting._tick_text_italic == ap.Boolean(True)
        assert setting._line_color == ap.String("#333333")
        assert setting._line_thickness == ap.Int(2)
        assert setting._line_alpha == ap.Number(0.7)
        assert setting._is_display_axis_label == ap.Boolean(False)
        assert setting._y_axis_label_position == ap.YAxisLabelPosition.OUTER_BOTTOM
        assert setting._axis_label_font_size == ap.Int(15)
        assert setting._axis_label_font_family == ap.Array([ap.String("Impact")])
        assert setting._axis_label_fill_color == ap.String("#777777")
        assert setting._axis_label_fill_alpha == ap.Number(0.9)
        assert setting._axis_label_bold == ap.Boolean(True)
        assert setting._top_margin == ap.Int(20)
        assert setting._left_margin == ap.Int(30)
        assert setting._axis_label_italic == ap.Boolean(True)
