from typing import Dict, Optional
from apysc.type.revert_interface import RevertInterface


class RevertableValue(RevertInterface):

    _snapshots: Dict[str, int] = {}

    def _make_snapshot(self, snapshot_name: str) -> None:
        """
        Make values snapshot.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._snapshots[snapshot_name] = 10
        self._set_snapshot_exists_val(snapshot_name=snapshot_name)

    def _revert(self, snapshot_name: str) -> None:
        """
        Revert values if snapshot exists.

        Parameters
        ----------
        snapshot_name : str
            Target snapshot name.
        """
        self._delete_snapshot_exists_val(snapshot_name=snapshot_name)



class TestRevertInterface:

    def test__is_snapshot_exists(self) -> None:
        revertable_value = RevertableValue()
        revertable_value._set_snapshot_exists_val(
            snapshot_name='snapshot_1')
        assert revertable_value._is_snapshot_exists(
            snapshot_name='snapshot_1')

        assert not revertable_value._is_snapshot_exists(
            snapshot_name='snapshot_2')

    def test__set_snapshot_exists_val(self) -> None:
        revertable_value = RevertableValue()
        revertable_value._set_snapshot_exists_val(
            snapshot_name='snapshot_1')
        assert revertable_value._snapshot_exists['snapshot_1']

    def test__delete_snapshot_exists_val(self) -> None:
        revertable_value = RevertableValue()
        revertable_value._set_snapshot_exists_val(
            snapshot_name='snapshot_1')
        revertable_value._delete_snapshot_exists_val(
            snapshot_name='snapshot_1')
        assert 'snapshot_1' not in revertable_value._snapshot_exists

        revertable_value._delete_snapshot_exists_val(
            snapshot_name='snapshot_2')
        assert 'snapshot_2' not in revertable_value._snapshot_exists
