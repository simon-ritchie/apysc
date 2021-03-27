from random import randint

import pytest
from retrying import retry

from apysc.display import Sprite
from apysc.display import Stage
from tests import testing_helper


class TestParentInterface:

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_parent(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        assert sprite.parent == stage

        with pytest.raises(ValueError):  # type: ignore
            sprite.parent = 100

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_remove_from_parent(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        sprite.remove_from_parent()
        assert stage.num_children == 0

        testing_helper.assert_raises(
            expected_error_class=ValueError,
            func_or_method=sprite.remove_from_parent,
        )

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_snapshot(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        snapshot_name: str = 'snapshot_1'
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert sprite._parent_snapshots[snapshot_name] == stage

        stage.remove_child(child=sprite)
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert sprite._parent_snapshots[snapshot_name] == stage

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__revert(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        snapshot_name: str = 'snapshot_1'
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        stage.remove_child(child=sprite)
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.parent == stage

        sprite.parent = None
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.parent == None
