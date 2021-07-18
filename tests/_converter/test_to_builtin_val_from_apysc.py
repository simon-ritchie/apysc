import apysc as ap
from apysc._converter import to_builtin_val_from_apysc


def test_get_builtin_str_from_apysc_val() -> None:
    builtin_val: str = \
        to_builtin_val_from_apysc.get_builtin_str_from_apysc_val(
            string='Hello')
    assert builtin_val == 'Hello'
    assert isinstance(builtin_val, str)

    builtin_val = to_builtin_val_from_apysc.get_builtin_str_from_apysc_val(
        string=ap.String('World'))
    assert builtin_val == 'World'
    assert isinstance(builtin_val, str)
