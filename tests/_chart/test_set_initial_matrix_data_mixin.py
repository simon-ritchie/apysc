from typing import Dict
from typing import List
from typing import Union

import apysc as ap
from apysc._chart import set_initial_matrix_data_mixin
from apysc._testing.testing_helper import apply_test_settings


@apply_test_settings()
def test__convert_list_to_array() -> None:
    data: List[Dict[str, Union[int, float, str]]] = [
        {
            "a": 10,
            "b": 20.5,
            "c": "1970-01-01",
        },
        {
            "a": 30,
            "b": 40.5,
            "c": "1970-01-02",
        },
    ]
    data_: ap.Array[
        ap.Dictionary[str, Union[ap.Int, ap.Number, ap.String]]
    ] = set_initial_matrix_data_mixin._convert_list_to_array(
        data=data,
        variable_name_suffix="test_suffix",
    )
    assert data_._variable_name_suffix == "test_suffix"
    assert data_._value[0]._variable_name_suffix == "test_suffix"
    assert data_._value[1]._variable_name_suffix == "test_suffix"
    assert data_ == ap.Array(
        [
            ap.Dictionary(
                {
                    "a": ap.Int(10),
                    "b": ap.Number(20.5),
                    "c": ap.String("1970-01-01"),
                },
            ),
            ap.Dictionary(
                {
                    "a": ap.Int(30),
                    "b": ap.Number(40.5),
                    "c": ap.String("1970-01-02"),
                },
            ),
        ]
    )
