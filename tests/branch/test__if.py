from typing import Any, Dict
from apysc.branch import If
from apysc.type import Boolean, Int
from tests import testing_helper


class TestIf:

    def test___init__(self) -> None:
        boolean_1: Boolean = Boolean(True)
        locals_: Dict[str, Any] = locals()
        globals_: Dict[str, Any] = globals()
        if_: If = If(
            condition=boolean_1, locals_=locals_, globals_=globals_)
        assert if_._condition
        testing_helper.assert_attrs(
            expected_attrs={
                '_condition': boolean_1,
                '_locals': locals_,
                '_globals': globals_,
            },
            any_obj=if_)

    def test___enter__(self) -> None:
        int_1: Int = Int(10)
        int_2: Int = Int(20)
        locals_: Dict[str, Any] = {'value1': int_1}
        globals_: Dict[str, Any] = {'value2': int_2}
        boolean_1: Boolean = Boolean(True)
        with If(condition=boolean_1, locals_=locals_, globals_=globals_):
            pass
        snapshot_name: str = list(int_1._value_snapshots.keys())[0]
        assert int_1._value_snapshots[snapshot_name] == 10
        assert int_2._value_snapshots[snapshot_name] == 20
