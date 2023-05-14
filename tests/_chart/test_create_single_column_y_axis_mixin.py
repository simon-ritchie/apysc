from typing import Union
import apysc as ap
from apysc._chart.create_single_column_y_axis_mixin import CreateSingleColumnYAxisMixIn
from apysc._testing.testing_helper import apply_test_settings
# from apysc._


class TestCreateSingleColumnYAxisMixIn:
    @apply_test_settings()
    def test__get_y_min(self) -> None:
        mixin: CreateSingleColumnYAxisMixIn = CreateSingleColumnYAxisMixIn()
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
        y_min: ap.Number = mixin._get_y_min(
            data=data, y_axis_column_name="a", variable_name_suffix="test_suffix"
        )
        assert isinstance(y_min, ap.Number)
        assert SUFFIX in y_min._variable_name_suffix
