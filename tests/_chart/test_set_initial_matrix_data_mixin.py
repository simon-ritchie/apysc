from typing import Dict
from typing import List
from typing import Union

import apysc as ap
from apysc._chart import set_initial_matrix_data_mixin
from apysc._chart.set_initial_matrix_data_mixin import SetInitialMatrixDataMixIn
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
        ap.Dictionary[ap.String, Union[ap.Int, ap.Number, ap.String]]
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
                    ap.String("a"): ap.Int(10),
                    ap.String("b"): ap.Number(20.5),
                    ap.String("c"): ap.String("1970-01-01"),
                },
            ),
            ap.Dictionary(
                {
                    ap.String("a"): ap.Int(30),
                    ap.String("b"): ap.Number(40.5),
                    ap.String("c"): ap.String("1970-01-02"),
                },
            ),
        ]
    )


class TestSetInitialMatrixDataMixIn:
    @apply_test_settings()
    def test__set_initial_matrix_data(self) -> None:
        mixin: SetInitialMatrixDataMixIn = SetInitialMatrixDataMixIn()
        mixin._set_initial_matrix_data(
            data=[
                {
                    "a": 10,
                    "b": 10.5,
                    "c": "1970-01-01",
                },
                {
                    "a": 20,
                    "b": 20.5,
                    "c": "1970-01-03",
                }
            ],
            variable_name_suffix="test_suffix",
        )
        arr_data: ap.Array[
            ap.Dictionary[ap.String, Union[ap.Int, ap.Number, ap.String]]
        ] = ap.Array(
            [
                ap.Dictionary(
                    {
                        ap.String("a"): ap.Int(10),
                        ap.String("b"): ap.Number(10.5),
                        ap.String("c"): ap.String("1970-01-01"),
                    },
                ),
                ap.Dictionary(
                    {
                        ap.String("a"): ap.Int(20),
                        ap.String("b"): ap.Number(20.5),
                        ap.String("c"): ap.String("1970-01-03"),
                    },
                ),
            ],
        )
        assert mixin._matrix_data == arr_data
        assert "test_suffix" in mixin._matrix_data.variable_name

        mixin = SetInitialMatrixDataMixIn()
        mixin._set_initial_matrix_data(
            data=arr_data,
            variable_name_suffix="test_suffix",
        )
        assert mixin._matrix_data == arr_data
