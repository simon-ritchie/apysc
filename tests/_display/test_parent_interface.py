from random import randint

import pytest
from retrying import retry

import apysc as ap
from apysc._expression import expression_file_util


class TestParentInterface:

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_parent(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        stage.add_child(child=sprite)
        assert sprite.parent == stage

        with pytest.raises(ValueError):  # type: ignore
            sprite.parent = 100

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test_remove_from_parent(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        sprite.remove_from_parent()
        assert stage.num_children == 0
        assert sprite.parent is None

        expression_file_util.empty_expression_dir()
        sprite.remove_from_parent()
        expression: str = expression_file_util.get_current_expression()
        assert f'removeElement({sprite.variable_name}' in expression

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__make_snapshot(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        stage.add_child(child=sprite)
        snapshot_name: str = 'snapshot_1'
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert sprite._parent_snapshots[snapshot_name] == stage

        stage.remove_child(child=sprite)
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert sprite._parent_snapshots[snapshot_name] == stage

    @retry(stop_max_attempt_number=15, wait_fixed=randint(10, 3000))
    def test__revert(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite(stage=stage)
        stage.add_child(child=sprite)
        snapshot_name: str = 'snapshot_1'
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        stage.remove_child(child=sprite)
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.parent == stage

        sprite.parent = None
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.parent is None
