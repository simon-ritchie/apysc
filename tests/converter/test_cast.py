from apysc.converter import cast
from apysc import Int
from apysc import Number


def test_to_int_from_float() -> None:
    int_val_1: int = cast.to_int_from_float(int_or_float=100)
    assert isinstance(int_val_1, int)
    assert int_val_1 == 100

    int_val_2: int = cast.to_int_from_float(int_or_float=200.5)
    assert isinstance(int_val_2, int)
    assert int_val_2 == 200

    int_val_3: Int = cast.to_int_from_float(int_or_float=Number(10.5))
    assert isinstance(int_val_3, Int)
    assert int_val_3 == 10


def test_to_float_from_int() -> None:
    float_val_1: float = cast.to_float_from_int(int_or_float=100)
    assert isinstance(float_val_1, float)
    assert float_val_1 == 100.0

    float_val_2: float = cast.to_float_from_int(int_or_float=100.5)
    assert float_val_2 == 100.5

    number_val_1: Number = cast.to_float_from_int(int_or_float=Int(10))
    assert isinstance(number_val_1, Number)
    assert number_val_1 == 10.0


def test_to_bool_from_int() -> None:
    bool_val: bool = cast.to_bool_from_int(integer=0)
    assert not bool_val
    bool_val = cast.to_bool_from_int(integer=1)
    assert bool_val
