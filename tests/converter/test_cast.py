from apyscript.converter import cast


def test_to_int_from_float() -> None:
    int_val: int = cast.to_int_from_float(int_or_float=100)
    assert isinstance(int_val, int)
    assert int_val == 100

    int_val = cast.to_int_from_float(int_or_float=200.5)
    assert isinstance(int_val, int)
    assert int_val == 200
