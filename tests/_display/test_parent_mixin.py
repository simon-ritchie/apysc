import pytest

import apysc as ap
from apysc._expression import expression_data_util
from apysc._testing.testing_helper import apply_test_settings


class TestParentMixIn:
    @apply_test_settings()
    def test_parent(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite)
        assert sprite.parent == stage

        with pytest.raises(ValueError):  # type: ignore
            sprite.parent = 100  # type: ignore

    @apply_test_settings()
    def test_remove_from_parent(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        sprite.remove_from_parent()
        assert stage.num_children == 0
        assert sprite.parent is None

        ap.Stage()
        sprite.remove_from_parent()
        expression: str = expression_data_util.get_current_expression()
        assert f"removeElement({sprite.variable_name}" in expression

    @apply_test_settings()
    def test__make_snapshot(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite)
        snapshot_name: str = "snapshot_1"
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        if sprite._parent_snapshots is None:
            raise AssertionError()
        assert sprite._parent_snapshots[snapshot_name] == stage

        stage.remove_child(child=sprite)
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        assert sprite._parent_snapshots[snapshot_name] == stage

    @apply_test_settings()
    def test__revert(self) -> None:
        stage: ap.Stage = ap.Stage()
        sprite: ap.Sprite = ap.Sprite()
        stage.add_child(child=sprite)
        snapshot_name: str = "snapshot_1"
        sprite._run_all_make_snapshot_methods(snapshot_name=snapshot_name)
        stage.remove_child(child=sprite)
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.parent == stage

        sprite.parent = None
        sprite._run_all_revert_methods(snapshot_name=snapshot_name)
        assert sprite.parent is None
