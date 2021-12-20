from random import randint

from retrying import retry

import apysc as ap
from apysc._geom.relative_interface import RelativeInterface


class TestRelativeInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_relative(self) -> None:
        interface: RelativeInterface = RelativeInterface()
        interface._relative = ap.Boolean(False)
        interface.relative = ap.Boolean(True)
        assert interface.relative

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        interface: RelativeInterface = RelativeInterface()
        interface._relative = ap.Boolean(True)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert interface._relative_snapshots[snapshot_name]

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        interface: RelativeInterface = RelativeInterface()
        interface._relative = ap.Boolean(True)
        snapshot_name: str = interface._get_next_snapshot_name()
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.relative

        interface._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        interface.relative = ap.Boolean(False)
        interface._run_all_revert_methods(snapshot_name=snapshot_name)
        assert interface.relative

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__initialize_relative_if_not_initialized(self) -> None:
        interface: RelativeInterface = RelativeInterface()
        interface._initialize_relative_if_not_initialized()
        assert not interface.relative

        interface.relative = ap.Boolean(True)
        interface._initialize_relative_if_not_initialized()
        assert interface.relative
