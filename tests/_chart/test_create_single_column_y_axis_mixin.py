from typing import Union
import apysc as ap
from apysc._chart.create_single_column_y_axis_mixin import CreateSingleColumnYAxisMixIn
from apysc._chart import create_single_column_y_axis_mixin
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._chart import chart_const


@apply_test_settings()
def test__get_y_min() -> None:
    expression_data_util.empty_expression()
    data: ap.Array[ap.Dictionary[str, Union[ap.Int, ap.Number, ap.String]]]
    SUFFIX: str = "test_suffix"
    data = ap.Array(
        [
            ap.Dictionary(
                {"a": ap.Int(10, variable_name_suffix=SUFFIX), "b": ap.Number(20.5)}
            ),
            ap.Dictionary(
                {"a": ap.Int(30, variable_name_suffix=SUFFIX), "b": ap.Number(40.5)}
            ),
            ap.Dictionary(
                {"a": ap.Int(5, variable_name_suffix=SUFFIX), "b": ap.Number(5.5)}
            ),
        ]
    )
    y_min: ap.Number = create_single_column_y_axis_mixin._calculate_y_min_from_data(
        data=data, y_axis_column_name="a", variable_name_suffix="test_suffix"
    )
    assert isinstance(y_min, ap.Number)
    assert SUFFIX in y_min._variable_name_suffix
    expression: str = expression_data_util.get_current_expression()
    assert ".min" in expression


@apply_test_settings()
def test__extract_column_values_from_data() -> None:
    expression_data_util.empty_expression()
    data = ap.Array(
        [
            ap.Dictionary(
                {
                    "a": ap.Int(10, variable_name_suffix="test_suffix"),
                    "b": ap.Number(20.5),
                },
            ),
            ap.Dictionary(
                {
                    "a": ap.Int(30, variable_name_suffix="test_suffix"),
                    "b": ap.Number(40.5),
                },
            ),
        ]
    )
    values: ap.Array[
        Union[ap.Int, ap.Number]
    ] = create_single_column_y_axis_mixin._extract_column_values_from_data(
        data=data,
        column_name="a",
        variable_name_suffix="test_suffix",
    )
    assert values._value[0] == ap.Int(10)
    assert values._variable_name_suffix == "test_suffix"
    expression: str = expression_data_util.get_current_expression()
    assert "for (" in expression


@apply_test_settings()
def test__calculate_y_max_from_data() -> None:
    expression_data_util.empty_expression()
    data = ap.Array(
        [
            ap.Dictionary(
                {
                    "a": ap.Int(10, variable_name_suffix="test_suffix"),
                    "b": ap.Number(20.5),
                },
            ),
            ap.Dictionary(
                {
                    "a": ap.Int(30, variable_name_suffix="test_suffix"),
                    "b": ap.Number(40.5),
                },
            ),
        ]
    )
    y_max: ap.Number = create_single_column_y_axis_mixin._calculate_y_max_from_data(
        data=data,
        y_axis_column_name="a",
        variable_name_suffix="test_suffix",
    )
    assert isinstance(y_max, ap.Number)
    assert "test_suffix" in y_max._variable_name_suffix
    expression: str = expression_data_util.get_current_expression()
    assert ".max" in expression


@apply_test_settings()
def test__calculate_y_axis_height() -> None:
    expression_data_util.empty_expression()
    y_axis_height: ap.Int = create_single_column_y_axis_mixin._calculate_y_axis_height(
        chart_height=ap.Int(500),
        vertical_padding=ap.Int(10),
        tick_text_font_size=ap.Int(10),
        axis_label_font_size=ap.Int(20),
        is_display_axis_label=ap.Boolean(False),
        variable_name_suffix="test_suffix",
    )
    assert y_axis_height._variable_name_suffix == "test_suffix"
    assert y_axis_height < 500


@apply_test_settings()
def test__calculate_y_axis_ticks_num() -> None:
    expression_data_util.empty_expression()
    y_axis_ticks_num: ap.Int = (
        create_single_column_y_axis_mixin._calculate_y_axis_ticks_num(
            y_axis_height=ap.Int(500),
            tick_max_num=None,
            tick_text_font_size=ap.Int(20),
            variable_name_suffix="test_suffix",
        )
    )
    assert y_axis_ticks_num == ap.Int(9)

    y_axis_ticks_num = create_single_column_y_axis_mixin._calculate_y_axis_ticks_num(
        y_axis_height=ap.Int(500),
        tick_max_num=ap.Int(5),
        tick_text_font_size=ap.Int(20),
        variable_name_suffix="test_suffix",
    )
    assert y_axis_ticks_num == ap.Int(5)
    assert y_axis_ticks_num._variable_name_suffix == "test_suffix"
