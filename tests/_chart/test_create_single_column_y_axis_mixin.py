from typing import Union

import apysc as ap
from apysc._chart import create_single_column_y_axis_mixin
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises


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
    data: ap.Array[ap.Dictionary[str, Union[ap.Int, ap.Number, ap.String]]] = ap.Array(
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
    data: ap.Array[ap.Dictionary[str, Union[ap.Int, ap.Number, ap.String]]] = ap.Array(
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


@apply_test_settings()
def test__calculate_y_axis_ticks_y_coordinates() -> None:
    y_axis_ticks_y_coordinates: ap.Array[
        ap.Number
    ] = create_single_column_y_axis_mixin._calculate_y_axis_ticks_y_coordinates(
        vertical_padding=ap.Int(20),
        y_axis_height=ap.Int(600),
        y_axis_ticks_num=ap.Int(5),
        variable_name_suffix="test_suffix",
    )
    assert isinstance(y_axis_ticks_y_coordinates[0], ap.Number)
    assert y_axis_ticks_y_coordinates._variable_name_suffix == "test_suffix"


@apply_test_settings()
def test__extract_text_value_from_data_dict() -> None:
    expression_data_util.empty_expression()
    int_value: ap.Int = ap.Int(10)
    number_value: ap.Number = ap.Number(20.5)
    str_value: ap.String = ap.String("test")
    text_value: ap.String = (
        create_single_column_y_axis_mixin._extract_text_value_from_data_dict(
            data_dict=ap.Dictionary(
                {
                    "a": int_value,
                    "b": number_value,
                    "c": str_value,
                },
            ),
            y_axis_column_name="a",
        )
    )
    assert isinstance(text_value, ap.String)
    expression: str = expression_data_util.get_current_expression()
    assert f"String({int_value.variable_name});" in expression

    expression_data_util.empty_expression()
    text_value = create_single_column_y_axis_mixin._extract_text_value_from_data_dict(
        data_dict=ap.Dictionary(
            {
                "a": int_value,
                "b": number_value,
                "c": str_value,
            },
        ),
        y_axis_column_name="b",
    )
    assert isinstance(text_value, ap.String)
    expression = expression_data_util.get_current_expression()
    assert f"String({number_value.variable_name});" in expression

    expression_data_util.empty_expression()
    text_value = create_single_column_y_axis_mixin._extract_text_value_from_data_dict(
        data_dict=ap.Dictionary(
            {
                "a": int_value,
                "b": number_value,
                "c": str_value,
            },
        ),
        y_axis_column_name="c",
    )
    assert isinstance(text_value, ap.String)
    expression = expression_data_util.get_current_expression()
    assert "String(" not in expression

    assert_raises(
        expected_error_class=TypeError,
        callable_=create_single_column_y_axis_mixin._extract_text_value_from_data_dict,
        match="A specified dictionary's value must be an `ap.Int`,",
        data_dict=ap.Dictionary(
            {
                "a": 10,
            },
        ),
        y_axis_column_name="a",
    )


@apply_test_settings()
def test__calculate_y_axis_max() -> None:
    y_axis_max: Union[
        ap.Int, ap.Number
    ] = create_single_column_y_axis_mixin._calculate_y_axis_max(
        y_max=ap.Number(100),
        in_value_y_max=ap.Number(80.5),
    )
    assert y_axis_max == ap.Number(100)

    y_axis_max = create_single_column_y_axis_mixin._calculate_y_axis_max(
        y_max=None,
        in_value_y_max=ap.Number(80.5),
    )
    assert y_axis_max == ap.Number(80.5) * 1.1


@apply_test_settings()
def test__apply_x_coordinate_to_y_axis_ticks_texts() -> None:
    y_axis_min: ap.Number = create_single_column_y_axis_mixin._calculate_y_axis_min(
        y_min=ap.Number(10.5),
        in_value_y_min=ap.Number(20.5),
    )
    assert y_axis_min == ap.Number(10.5)

    y_axis_min = create_single_column_y_axis_mixin._calculate_y_axis_min(
        y_min=None,
        in_value_y_min=ap.Number(20.5),
    )
    assert y_axis_min == ap.Number(20.5)


@apply_test_settings()
def test__create_y_axis_texts_values() -> None:
    expression_data_util.empty_expression()
    y_axis_text_values: ap.Array[
        ap.String
    ] = create_single_column_y_axis_mixin._create_y_axis_texts_values(
        y_axis_min=ap.Number(0),
        y_axis_max=ap.Number(100),
        ticks_num=ap.Int(5),
        variable_name_suffix="test_suffix",
    )
    assert isinstance(y_axis_text_values[0], ap.String)
    expression: str = expression_data_util.get_current_expression()
    assert "for (" in expression
    assert "test_suffix" in y_axis_text_values.variable_name
