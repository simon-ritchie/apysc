import apysc as ap
from apysc._testing.testing_helper import apply_test_settings


class TestYAxisSingleColumnSettings:
    @apply_test_settings()
    def test___init__(self) -> None:
        settings: ap.YAxisSingleColumnSettings = ap.YAxisSingleColumnSettings(
            y_axis_column_name="test_column_1",
            y_min=0,
            y_max=100,
            tick_max_num=20,
            tick_text_font_family=["Arial"],
            tick_text_fill_color="#666",
            tick_text_fill_alpha=0.5,
            tick_text_bold=True,
            tick_text_italic=True,
            tick_text_max_num_of_decimal_places=2,
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
            variable_name_suffix="test_suffix",
        )
        assert settings._y_axis_column_name == ap.String("test_column_1")
        assert settings._y_min == ap.Number(0)
        if settings._y_min is not None:
            assert settings._y_min._variable_name_suffix == "test_suffix"
        assert settings._y_max == ap.Number(100)
        assert settings._tick_max_num == ap.Int(20)
        assert settings._tick_text_font_family == ap.Array([ap.String("Arial")])
        assert settings._tick_text_fill_color == ap.String("#666666")
        assert settings._tick_text_fill_alpha == ap.Number(0.5)
        assert settings._tick_text_bold == ap.True_
        assert settings._tick_text_italic == ap.True_
        assert settings._tick_text_max_num_of_decimal_places == ap.Int(2)
        assert settings._line_color == ap.String("#333333")
        assert settings._line_thickness == ap.Int(2)
        assert settings._line_alpha == ap.Number(0.7)
        assert settings._is_display_axis_label == ap.Boolean(False)
        assert settings._y_axis_label_position == ap.YAxisLabelPosition.OUTER_BOTTOM
        assert settings._axis_label_font_size == ap.Int(15)
        assert settings._axis_label_font_family == ap.Array([ap.String("Impact")])
        assert settings._axis_label_fill_color == ap.String("#777777")
        assert settings._axis_label_fill_alpha == ap.Number(0.9)
        assert settings._axis_label_bold == ap.True_
        assert settings._axis_label_italic == ap.True_

        settings = ap.YAxisSingleColumnSettings(
            y_axis_column_name=ap.String("test_column_2"),
            y_min=ap.Number(10),
            y_max=ap.Number(200),
            tick_max_num=ap.Int(25),
            tick_text_font_family=ap.Array([ap.String("Impact")]),
            tick_text_fill_color=ap.String("#777"),
            tick_text_fill_alpha=ap.Number(0.7),
            tick_text_bold=ap.Boolean(False),
            tick_text_italic=ap.Boolean(False),
            tick_text_max_num_of_decimal_places=ap.Int(3),
            line_color=ap.String("#555"),
            line_thickness=ap.Int(3),
            line_alpha=ap.Number(0.8),
            is_display_axis_label=ap.True_,
            axis_label_font_size=ap.Int(16),
            axis_label_font_family=ap.Array([ap.String("Helvetica")]),
            axis_label_fill_color=ap.String("#888"),
            axis_label_fill_alpha=ap.Number(0.6),
            axis_label_bold=ap.Boolean(False),
            axis_label_italic=ap.Boolean(False),
        )
        assert settings._y_axis_column_name == ap.String("test_column_2")
        assert settings._y_min == ap.Number(10)
        assert settings._y_max == ap.Number(200)
        assert settings._tick_max_num == ap.Int(25)
        assert settings._tick_text_font_family == ap.Array([ap.String("Impact")])
        assert settings._tick_text_fill_color == ap.String("#777777")
        assert settings._tick_text_fill_alpha == ap.Number(0.7)
        assert settings._tick_text_bold == ap.Boolean(False)
        assert settings._tick_text_italic == ap.Boolean(False)
        assert settings._tick_text_max_num_of_decimal_places == ap.Int(3)
        assert settings._line_color == ap.String("#555555")
        assert settings._line_thickness == ap.Int(3)
        assert settings._line_alpha == ap.Number(0.8)
        assert settings._is_display_axis_label == ap.True_
        assert settings._axis_label_font_size == ap.Int(16)
        assert settings._axis_label_font_family == ap.Array([ap.String("Helvetica")])
        assert settings._axis_label_fill_color == ap.String("#888888")
        assert settings._axis_label_fill_alpha == ap.Number(0.6)
        assert settings._axis_label_bold == ap.Boolean(False)
        assert settings._axis_label_italic == ap.Boolean(False)
