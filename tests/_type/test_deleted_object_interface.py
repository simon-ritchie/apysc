from random import randint

from retrying import retry
from apysc._testing.testing_helper import assert_raises

from apysc._type.deleted_object_interface import DeletedObjectInterface, _DisabledObjectError


class TestDeletedObjectInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__is_deleted_object(self) -> None:
        interface: DeletedObjectInterface = DeletedObjectInterface()
        assert not interface._is_deleted_object

        interface._is_deleted_object = True
        assert interface._is_deleted_object

        class _TestClass(DeletedObjectInterface):

            def _test_func(self, a: int) -> int:
                return a * 2

        instance: _TestClass = _TestClass()
        instance._is_deleted_object = True
        assert_raises(
            expected_error_class=_DisabledObjectError,
            callable_=instance._test_func,
            a=100,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: DeletedObjectInterface = DeletedObjectInterface()
        interface._is_deleted_object = True
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._is_deleted_object_snapshot[snapshot_name] = True

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: DeletedObjectInterface = DeletedObjectInterface()
        interface._is_deleted_object = True
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._is_deleted_object = False
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface._is_deleted_object

        interface._is_deleted_object = False
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not interface._is_deleted_object

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__disable_each_methods(self) -> None:

        class _TestClass(DeletedObjectInterface):

            def _test_func(self, a: int) -> int:
                return a * 2

        test_instance: _TestClass = _TestClass()
        test_instance._disable_each_method()
        assert_raises(
            expected_error_class=_DisabledObjectError,
            callable_=test_instance._test_func,
            a=100,
        )

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__disabled_method(self) -> None:
        interface: DeletedObjectInterface = DeletedObjectInterface()
        assert_raises(
            expected_error_class=_DisabledObjectError,
            callable_=interface._disabled_method,
            a=100)
