from random import randint

from retrying import retry

import apysc as ap
from apysc._converter import to_apysc_val_from_builtin


@retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
def test_get_copied_int_from_builtin_val() -> None:
    copied: ap.Int = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
        integer=10)
    assert copied == 10
    assert isinstance(copied, ap.Int)

    int_1: ap.Int = ap.Int(20)
    copied = to_apysc_val_from_builtin.get_copied_int_from_builtin_val(
        integer=int_1)
    assert copied == 20
    assert isinstance(copied, ap.Int)
    assert int_1.variable_name != copied.variable_name
