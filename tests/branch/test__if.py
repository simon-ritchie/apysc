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

    def test__make_snapshots_of_each_scope_vars(self) -> None:
        int_1: Int = Int(10)
        int_2: Int = Int(20)
        int_3: Int = Int(40)
        locals_: Dict[str, Any] = {
            'value1': int_1,
            'value2': int_2,
            'value3': 30,
        }
        globals_: Dict[str, Any] = {
            'value_4': int_1,
            'value_5': int_3,
        }
        if_: If = If(
            condition=Boolean(True), locals_=locals_, globals_=globals_)
        snapshot_name: str = if_._make_snapshots_of_each_scope_vars()
        assert int_1._value_snapshots[snapshot_name] == 10
        assert int_2._value_snapshots[snapshot_name] == 20
        assert int_3._value_snapshots[snapshot_name] == 40
