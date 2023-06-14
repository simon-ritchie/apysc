from typing import Union
import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._loop import loop_util


@apply_test_settings()
def test_get_dict_key_for_loop() -> None:
    dict_key: Union[ap.String, ap.Int, ap.Boolean] = loop_util.get_dict_key_for_loop(
        dict_key_type=str,
    )
    assert dict_key == ap.String("")

    dict_key = loop_util.get_dict_key_for_loop(
        dict_key_type=ap.String,
    )
    assert dict_key == ap.String("")

    dict_key = loop_util.get_dict_key_for_loop(
        dict_key_type=int,
    )
    assert dict_key == ap.Int(0)

    dict_key = loop_util.get_dict_key_for_loop(
        dict_key_type=ap.Int,
    )
    assert dict_key == ap.Int(0)

    dict_key = loop_util.get_dict_key_for_loop(
        dict_key_type=bool,
    )
    assert dict_key == ap.Boolean(False)

    dict_key = loop_util.get_dict_key_for_loop(
        dict_key_type=ap.Boolean,
    )
    assert dict_key == ap.Boolean(False)
