from apysc import For, Array
from tests import testing_helper


class TestFor:

    def test___init__(self) -> None:
        arr: Array = Array([1, 2, 3])
        for_: For = For(
            arr=arr, locals_={'value_1': 1},
            globals_={'value_2': 2})
        testing_helper.assert_attrs(
            expected_attrs={
                '_arr': arr,
                '_locals': {'value_1': 1},
                '_globals': {'value_2': 2},
            },
            any_obj=for_)
