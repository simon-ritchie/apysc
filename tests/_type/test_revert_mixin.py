from typing import Any
from typing import Dict
from typing import List, Optional

import apysc as ap
from apysc._testing.testing_helper import apply_test_settings
from apysc._type import revert_mixin
from apysc._type.revert_mixin import RevertMixIn


class NotRevertableValue:
    ...


class RevertableValue1(RevertMixIn):

    _value1: int = 10
    _snapshots1: Optional[Dict[str, int]] = None

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._snapshots1 is None:
            self._snapshots1 = {}
        self._snapshots1[snapshot_name] = self._value1

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._snapshots1 is None:
            self._snapshots1 = {}
        self._value1 = self._snapshots1[snapshot_name]


class RevertableValue2(RevertMixIn):

    _value2: int = 20
    _snapshots2: Optional[Dict[str, int]] = None

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._snapshots2 is None:
            self._snapshots2 = {}
        self._snapshots2[snapshot_name] = self._value2

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._snapshots2 is None:
            self._snapshots2 = {}
        self._value2 = self._snapshots2[snapshot_name]


class RevertableValue3(NotRevertableValue, RevertableValue1, RevertableValue2):

    _value3: int = 30
    _snapshots3: Optional[Dict[str, int]] = None

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make value's snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._snapshots3 is None:
            self._snapshots3 = {}
        self._snapshots3[snapshot_name] = self._value3

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if a snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        if self._snapshots3 is None:
            self._snapshots3 = {}
        self._value3 = self._snapshots3[snapshot_name]


class TestRevertMixIn:
    def test__is_snapshot_exists(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._set_snapshot_exists_val(snapshot_name="snapshot_1")
        assert revertable_value._snapshot_exists(snapshot_name="snapshot_1")

        assert not revertable_value._snapshot_exists(snapshot_name="snapshot_2")

    def test__set_snapshot_exists_val(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._set_snapshot_exists_val(snapshot_name="snapshot_1")
        assert revertable_value._snapshot_exists_["snapshot_1"]

    def test__delete_snapshot_exists_val(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._set_snapshot_exists_val(snapshot_name="snapshot_1")
        revertable_value._delete_snapshot_exists_val(snapshot_name="snapshot_1")
        assert "snapshot_1" not in revertable_value._snapshot_exists_

        revertable_value._delete_snapshot_exists_val(snapshot_name="snapshot_2")
        assert "snapshot_2" not in revertable_value._snapshot_exists_

    @apply_test_settings()
    def test__get_next_snapshot_name(self) -> None:
        from apysc._expression.var_names import SNAPSHOT

        revertable_value = RevertableValue1()
        snapshot_name_1: str = revertable_value._get_next_snapshot_name()
        assert snapshot_name_1.startswith(SNAPSHOT)

        snapshot_name_2: str = revertable_value._get_next_snapshot_name()
        assert snapshot_name_1 != snapshot_name_2

    @apply_test_settings()
    def test__initialize_ss_exists_val_if_not_initialized(self) -> None:
        revertable_value = RevertableValue1()
        revertable_value._initialize_ss_exists_val_if_not_initialized()
        assert revertable_value._snapshot_exists_ == {}

        revertable_value._snapshot_exists_["snapshot_1"] = True
        revertable_value._initialize_ss_exists_val_if_not_initialized()
        assert revertable_value._snapshot_exists_ == {"snapshot_1": True}

    @apply_test_settings()
    def test__run_all_make_snapshot_methods(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = "snapshot_1"
        revertable_value._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert revertable_value._snapshot_exists(snapshot_name=snapshot_name)
        if revertable_value._snapshots1 is None:
            raise AssertionError()
        assert revertable_value._snapshots1[snapshot_name] == 10
        if revertable_value._snapshots2 is None:
            raise AssertionError()
        assert revertable_value._snapshots2[snapshot_name] == 20
        if revertable_value._snapshots3 is None:
            raise AssertionError()
        assert revertable_value._snapshots3[snapshot_name] == 30

    @apply_test_settings()
    def test__run_all_revert_methods(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = "snapshot_1"
        revertable_value._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        revertable_value._value1 = 100
        revertable_value._value2 = 200
        revertable_value._value3 = 200
        revertable_value._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not revertable_value._snapshot_exists(snapshot_name=snapshot_name)
        assert revertable_value._value1 == 10
        assert revertable_value._value2 == 20
        assert revertable_value._value3 == 30

    @apply_test_settings()
    def test__run_base_cls_make_snapshot_methods_recursively(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = "snapshot_1"
        revertable_value._run_base_cls_make_snapshot_methods_recursively(
            class_=RevertableValue3, snapshot_name=snapshot_name
        )
        if revertable_value._snapshots1 is None:
            raise AssertionError()
        assert revertable_value._snapshots1[snapshot_name] == 10
        if revertable_value._snapshots2 is None:
            raise AssertionError()
        assert revertable_value._snapshots2[snapshot_name] == 20
        if revertable_value._snapshots3 is None:
            raise AssertionError()
        assert revertable_value._snapshots3[snapshot_name] == 30

    @apply_test_settings()
    def test__run_base_cls_revert_methods_recursively(self) -> None:
        revertable_value = RevertableValue3()
        snapshot_name: str = "snapshot_1"
        revertable_value._run_base_cls_make_snapshot_methods_recursively(
            class_=RevertableValue3, snapshot_name=snapshot_name
        )
        revertable_value._value1 = 100
        revertable_value._value2 = 200
        revertable_value._value3 = 300
        revertable_value._run_base_cls_revert_methods_recursively(
            class_=RevertableValue3, snapshot_name=snapshot_name
        )
        assert revertable_value._value1 == 10
        assert revertable_value._value2 == 20
        assert revertable_value._value3 == 30

    @apply_test_settings()
    def test__set_single_snapshot_val_to_dict(self) -> None:
        revertable_value = RevertableValue1()
        snapshot_name: str = "snapshot_1"
        revertable_value._set_single_snapshot_val_to_dict(
            dict_name="_snapshots1", value=10, snapshot_name=snapshot_name
        )
        if revertable_value._snapshots1 is None:
            raise AssertionError()
        assert revertable_value._snapshots1[snapshot_name] == 10
        revertable_value._set_snapshot_exists_val(snapshot_name=snapshot_name)

        revertable_value._set_single_snapshot_val_to_dict(
            dict_name="_snapshots1", value=20, snapshot_name=snapshot_name
        )
        assert revertable_value._snapshots1[snapshot_name] == 10

    @apply_test_settings()
    def test__get_snapshot_val_if_exists(self) -> None:
        revertable_value: RevertableValue1 = RevertableValue1()
        revertable_value._value1 = 20
        revertable_value._run_all_make_snapshot_methods(snapshot_name="snapshot_1")
        revertable_value._value1 = 30
        revertable_value._value1 = revertable_value._get_snapshot_val_if_exists(
            current_value=revertable_value._value1,
            snapshot_dict=revertable_value._snapshots1,
            snapshot_name="snapshot_1",
        )
        assert revertable_value._value1 == 20

        revertable_value._value1 = revertable_value._get_snapshot_val_if_exists(
            current_value=revertable_value._value1,
            snapshot_dict=revertable_value._snapshots1,
            snapshot_name="not_existing_snapshot",
        )
        assert revertable_value._value1 == 20


def test_make_snapshots_of_each_scope_vars() -> None:
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    int_3: ap.Int = ap.Int(40)
    locals_: Dict[str, Any] = {
        "value1": int_1,
        "value2": int_2,
        "value3": 30,
    }
    globals_: Dict[str, Any] = {
        "value_4": int_1,
        "value_5": int_3,
    }
    snapshot_name: str = revert_mixin.make_snapshots_of_each_scope_vars(
        locals_=locals_, globals_=globals_
    )
    assert int_1._value_snapshots[snapshot_name] == 10
    assert int_2._value_snapshots[snapshot_name] == 20
    assert int_3._value_snapshots[snapshot_name] == 40


def test_revert_each_scope_vars() -> None:
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    int_3: ap.Int = ap.Int(40)
    locals_: Dict[str, Any] = {
        "value1": int_1,
        "value2": int_2,
        "value3": 30,
    }
    globals_: Dict[str, Any] = {
        "value_4": int_1,
        "value_5": int_3,
    }
    snapshot_name: str = revert_mixin.make_snapshots_of_each_scope_vars(
        locals_=locals_, globals_=globals_
    )
    int_1.value = 100
    int_2.value = 200
    int_3.value = 400
    revert_mixin.revert_each_scope_vars(
        snapshot_name=snapshot_name, locals_=locals_, globals_=globals_
    )
    assert int_1._value == 10
    assert int_2._value == 20
    assert int_3._value == 40


def test_make_variables_snapshots() -> None:
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    variables: List[Any] = [int_1, int_2, int_1, 100]
    snapshot_name: str = revert_mixin.make_variables_snapshots(variables=variables)
    assert int_1._snapshot_exists(snapshot_name=snapshot_name)
    assert int_2._snapshot_exists(snapshot_name=snapshot_name)


def test_revert_variables() -> None:
    int_1: ap.Int = ap.Int(10)
    int_2: ap.Int = ap.Int(20)
    variables: List[Any] = [int_1, int_2, int_1, 100]
    snapshot_name: str = revert_mixin.make_variables_snapshots(variables=variables)
    int_1.value = 30
    int_2.value = 40
    revert_mixin.revert_variables(snapshot_name=snapshot_name, variables=variables)
    assert int_1._value == 10
    assert int_2._value == 20
