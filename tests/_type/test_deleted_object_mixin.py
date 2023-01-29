from apysc._testing.testing_helper import apply_test_settings
from apysc._testing.testing_helper import assert_raises
from apysc._type.deleted_object_mixin import DeletedObjectMixIn
from apysc._type.deleted_object_mixin import _DisabledObjectError


class TestDeletedObjectMixIn:
    @apply_test_settings()
    def test__is_deleted_object(self) -> None:
        mixin: DeletedObjectMixIn = DeletedObjectMixIn()
        assert not mixin._is_deleted_object

        mixin._is_deleted_object = True
        assert mixin._is_deleted_object

        class _TestClass(DeletedObjectMixIn):
            def _test_func(self, a: int) -> int:
                return a * 2

        instance: _TestClass = _TestClass()
        instance._is_deleted_object = True
        assert_raises(
            expected_error_class=_DisabledObjectError,
            callable_=instance._test_func,
            a=100,
        )

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        mixin: DeletedObjectMixIn = DeletedObjectMixIn()
        mixin._is_deleted_object = True
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._is_deleted_object_snapshot[snapshot_name] = True

    @apply_test_settings()
    def test__revert(self) -> None:
        mixin: DeletedObjectMixIn = DeletedObjectMixIn()
        mixin._is_deleted_object = True
        snapshot_name: str = mixin._get_next_snapshot_name()
        mixin._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        mixin._is_deleted_object = False
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert mixin._is_deleted_object

        mixin._is_deleted_object = False
        mixin._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not mixin._is_deleted_object

    @apply_test_settings()
    def test__disable_each_methods(self) -> None:
        class _TestClass(DeletedObjectMixIn):
            def _test_func(self, a: int) -> int:
                return a * 2

        test_instance: _TestClass = _TestClass()
        test_instance._disable_each_method()
        assert_raises(
            expected_error_class=_DisabledObjectError,
            callable_=test_instance._test_func,
            a=100,
        )

    @apply_test_settings()
    def test__disabled_method(self) -> None:
        mixin: DeletedObjectMixIn = DeletedObjectMixIn()
        assert_raises(
            expected_error_class=_DisabledObjectError,
            callable_=mixin._disabled_method,
            a=100,
        )
