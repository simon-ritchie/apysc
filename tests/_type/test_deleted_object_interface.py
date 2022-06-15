from random import randint

from retrying import retry

from apysc._type.deleted_object_interface import DeletedObjectInterface


class TestDeletedObjectInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_is_deleted_object(self) -> None:
        interface: DeletedObjectInterface = DeletedObjectInterface()
        assert not interface.is_deleted_object

        interface.is_deleted_object = True
        assert interface.is_deleted_object

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: DeletedObjectInterface = DeletedObjectInterface()
        interface.is_deleted_object = True
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface._is_deleted_object_snapshot[snapshot_name] = True

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: DeletedObjectInterface = DeletedObjectInterface()
        interface.is_deleted_object = True
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.is_deleted_object = False
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.is_deleted_object

        interface.is_deleted_object = False
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert not interface.is_deleted_object
