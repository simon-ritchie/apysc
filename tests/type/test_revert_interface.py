from typing import Optional
from apysc.type.revert_interface import RevertInterface


class RevertableValue(RevertInterface):

    _snapshot: Optional[int] = None

    def make_snapshot(self) -> None:
        """
        Make values snapshot.
        """
        self.snapshot_exists = True
        self._snapshot = 100

    def revert(self) -> None:
        """
        Revert values if snapshot exists.
        """
        if not self.snapshot_exists:
            return
        self._snapshot = None
        self.snapshot_exists = False


class TestRevertInterface:

    def test_snapshot_exists(self) -> None:
        revertable_value = RevertableValue()
        revertable_value.make_snapshot()
        assert revertable_value.snapshot_exists

        revertable_value.revert()
        assert not revertable_value.snapshot_exists
