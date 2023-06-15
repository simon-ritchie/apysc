from typing import Union
import apysc as ap
from apysc._testing.testing_helper import apply_test_settings, assert_raises
from apysc._loop import loop_util


@apply_test_settings()
def test_get_dict_key_for_loop() -> None:
    dict_key_1: str = loop_util.get_dict_key_for_loop(
        dict_key_type=str,
    )
    assert dict_key_1 == ""

    dict_key_2: ap.String = loop_util.get_dict_key_for_loop(
        dict_key_type=ap.String,
    )
    assert dict_key_2 == ap.String("")

    dict_key_3: int = loop_util.get_dict_key_for_loop(
        dict_key_type=int,
    )
    assert dict_key_3 == 0

    dict_key_4: ap.Int = loop_util.get_dict_key_for_loop(
        dict_key_type=ap.Int,
    )
    assert dict_key_4 == ap.Int(0)

    dict_key_5: bool = loop_util.get_dict_key_for_loop(
        dict_key_type=bool,
    )
    assert dict_key_5 == False

    dict_key_6: ap.Boolean = loop_util.get_dict_key_for_loop(
        dict_key_type=ap.Boolean,
    )
    assert dict_key_6 == ap.Boolean(False)

    assert_raises(
        expected_error_class=TypeError,
        callable_=loop_util.get_dict_key_for_loop,
        dict_key_type=list,
    )
