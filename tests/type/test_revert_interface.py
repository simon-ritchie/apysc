from random import randint
from typing import Any
from typing import Dict
from typing import List

from retrying import retry

from apysc import Int
from apysc.type import revert_interface
from apysc.type.revert_interface import RevertInterface


class NotRevertableValue:
    ...


class RevertableValue1(RevertInterface):

    _value1: int = 10
    _snapshots1: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_snapshots1'):
            self._snapshots1 = {}
        self._snapshots1[snapshot_name] = self._value1

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._value1 = self._snapshots1[snapshot_name]


class RevertableValue2(RevertInterface):

    _value2: int = 20
    _snapshots2: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_snapshots2'):
            self._snapshots2 = {}
        self._snapshots2[snapshot_name] = self._value2

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._value2 = self._snapshots2[snapshot_name]


class RevertableValue3(
        NotRevertableValue, RevertableValue1, RevertableValue2):

    _value3: int = 30
    _snapshots3: Dict[str, int]

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if not hasattr(self, '_snapshots3'):
            self._snapshots3 = {}
        self._snapshots3[snapshot_name] = self._value3

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._value3 = self._snapshots3[snapshot_name]


class TestRevertInterface:

    def test__is_snapshot_exists(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._set_snapshot_exists_val(
            snapshot_name='snapshot_1')
        assert revertable_value._snapshot_exists(
            snapshot_name='snapshot_1')

        assert not revertable_value._snapshot_exists(
            snapshot_name='snapshot_2')

    def test__set_snapshot_exists_val(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._set_snapshot_exists_val(
            snapshot_name='snapshot_1')
        assert revertable_value._snapshot_exists_['snapshot_1']

    def test__delete_snapshot_exists_val(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._set_snapshot_exists_val(
            snapshot_name='snapshot_1')
        revertable_value._delete_snapshot_exists_val(
            snapshot_name='snapshot_1')
        assert 'snapshot_1' not in revertable_value._snapshot_exists_

        revertable_value._delete_snapshot_exists_val(
            snapshot_name='snapshot_2')
        assert 'snapshot_2' not in revertable_value._snapshot_exists_

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__get_next_snapshot_name(self) -> None:
        from apysc.expression.var_names import SNAPSHOT
        revertable_value = RevertableValue1()
        snapshot_name_1: str = revertable_value._get_next_snapshot_name()
        assert snapshot_name_1.startswith(SNAPSHOT)

        snapshot_name_2: str = revertable_value._get_next_snapshot_name()
        assert snapshot_name_1 != snapshot_name_2

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_ss_exists_val_if_not_initialized(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._initialize_ss_exists_val_if_not_initialized()
        assert revertable_value._snapshot_exists_ == {}

        revertable_value._snapshot_exists_['snapshot_1'] = True
        revertable_value._initialize_ss_exists_val_if_not_initialized()
        assert revertable_value._snapshot_exists_ == {'snapshot_1': True}

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__run_all_make_snapshot_methods(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = 'snapshot_1'
        revertable_value._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        assert revertable_value._snapshot_exists(
            snapshot_name=snapshot_name)
        assert revertable_value._snapshots1[snapshot_name] == 10
        assert revertable_value._snapshots2[snapshot_name] == 20
        assert revertable_value._snapshots3[snapshot_name] == 30

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__run_all_revert_methods(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = 'snapshot_1'
        revertable_value._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name)
        revertable_value._value1 = 100
        revertable_value._value2 = 200
        revertable_value._value3 = 200
        revertable_value._run_all_revert_methods(
            snapshot_name=snapshot_name)
        assert not revertable_value._snapshot_exists(
            snapshot_name=snapshot_name)
        assert revertable_value._value1 == 10
        assert revertable_value._value2 == 20
        assert revertable_value._value3 == 30

    def test__run_base_cls_make_snapshot_methods_recursively(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = 'snapshot_1'
        revertable_value._run_base_cls_make_snapshot_methods_recursively(
            class_=RevertableValue3, snapshot_name=snapshot_name)
        assert revertable_value._snapshots1[snapshot_name] == 10
        assert revertable_value._snapshots2[snapshot_name] == 20
        assert revertable_value._snapshots3[snapshot_name] == 30

    def test__run_base_cls_revert_methods_recursively(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = 'snapshot_1'
        revertable_value._run_base_cls_make_snapshot_methods_recursively(
            class_=RevertableValue3, snapshot_name=snapshot_name)
        revertable_value._value1 = 100
        revertable_value._value2 = 200
        revertable_value._value3 = 300
        revertable_value._run_base_cls_revert_methods_recursively(
            class_=RevertableValue3, snapshot_name=snapshot_name)
        assert revertable_value._value1 == 10
        assert revertable_value._value2 == 20
        assert revertable_value._value3 == 30


def test_make_snapshots_of_each_scope_vars() -> None:
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
    snapshot_name: str = revert_interface.\
        make_snapshots_of_each_scope_vars(
            locals_=locals_, globals_=globals_)
    assert int_1._value_snapshots[snapshot_name] == 10
    assert int_2._value_snapshots[snapshot_name] == 20
    assert int_3._value_snapshots[snapshot_name] == 40


def test_revert_each_scope_vars() -> None:
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
    snapshot_name: str = revert_interface.make_snapshots_of_each_scope_vars(
        locals_=locals_, globals_=globals_)
    int_1.value = 100
    int_2.value = 200
    int_3.value = 400
    revert_interface.revert_each_scope_vars(
        snapshot_name=snapshot_name,
        locals_=locals_, globals_=globals_)
    assert int_1._value == 10
    assert int_2._value == 20
    assert int_3._value == 40


def test_make_variables_snapshots() -> None:
    int_1: Int = Int(10)
    int_2: Int = Int(20)
    variables: List[Any] = [int_1, int_2, int_1, 100]
    snapshot_name: str = revert_interface.make_variables_snapshots(
        variables=variables)
    assert int_1._snapshot_exists(snapshot_name=snapshot_name)
    assert int_2._snapshot_exists(snapshot_name=snapshot_name)


def test_revert_variables() -> None:
    int_1: Int = Int(10)
    int_2: Int = Int(20)
    variables: List[Any] = [int_1, int_2, int_1, 100]
    snapshot_name: str = revert_interface.make_variables_snapshots(
        variables=variables)
    int_1.value = 30
    int_2.value = 40
    revert_interface.revert_variables(
        snapshot_name=snapshot_name, variables=variables)
    assert int_1._value == 10
    assert int_2._value == 20
