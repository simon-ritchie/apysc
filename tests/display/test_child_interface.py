from random import randint

from retrying import retry

from apysc.display import Sprite
from apysc.display import Stage
from apysc.display.child_interface import ChildInterface
from apysc.display.display_object import DisplayObject
from apysc.expression import expression_file_util
from apysc.type import Array
from apysc.type import Boolean
from apysc.type import Int


class TestChildInterface:
    """Because of `VariableNameInterface` inheritance,
    each test will be executed with Stage and Sprite
    (ChildInterface subclasses).
    """

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_add_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        assert stage._children == Array([sprite])
        assert sprite.parent == stage

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_expression_of_add_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        expected: str = (
            f'{stage.variable_name}.add({sprite.variable_name});'
        )
        expression: str = expression_file_util.get_current_expression()
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_remove_child(self) -> None:
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        sprite_2: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_2)
        stage.remove_child(child=sprite_2)
        assert stage._children == Array([sprite_1])
        assert sprite_2.parent is None

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_expression_of_remove_child(self) -> None:
        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        stage.remove_child(child=sprite)
        expected: str = (
            f'{stage.variable_name}.removeElement({sprite.variable_name});'
        )
        expression: str = expression_file_util.get_current_expression()
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_contains(self) -> None:
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        assert stage.contains(child=sprite_1)

        sprite_2: Sprite = Sprite(stage=stage)
        assert not stage.contains(child=sprite_2)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_contains_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        result: Boolean = stage.contains(sprite_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{result._variable_name} = '
            f'{stage.variable_name}.has({sprite_1.variable_name});'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_num_children(self) -> None:
        stage: Stage = Stage()
        assert stage.num_children == 0
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        assert stage.num_children == 1
        sprite_2: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_2)
        assert stage.num_children == 2

        sprite_3: Sprite = Sprite(stage=stage)
        sprite_1.add_child(child=sprite_3)
        assert sprite_1.num_children == 1

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test_get_child_at(self) -> None:
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        child_1: DisplayObject = stage.get_child_at(index=0)
        assert child_1 == sprite_1

        child_2: DisplayObject = stage.get_child_at(index=1)
        assert not isinstance(child_2, Sprite)
        assert isinstance(child_2, DisplayObject)

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_num_children_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        num_children_1: Int = stage.num_children
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'{num_children_1.variable_name} = '
            f'{stage.variable_name}.children().length - 0;'
        )
        assert expected in expression

        sprite_2: Sprite = Sprite(stage=stage)
        sprite_1.add_child(child=sprite_2)
        num_children_2 = sprite_1.num_children
        expression = expression_file_util.get_current_expression()
        expected = (
            f'{num_children_2.variable_name} = '
            f'{sprite_1.variable_name}.children().length - 1;'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__append_get_child_at_expression(self) -> None:
        expression_file_util.remove_expression_file()
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        int_1: Int = Int(0)
        child_1: DisplayObject = stage.get_child_at(index=int_1)
        expression: str = expression_file_util.get_current_expression()
        expected: str = (
            f'var {child_1.variable_name} = '
            f'{stage.variable_name}.children()'
            f'[{int_1.variable_name} + 0];'
        )
        assert expected in expression

        sprite_2: Sprite = Sprite(stage=stage)
        sprite_1.add_child(child=sprite_2)
        child_2: DisplayObject = sprite_1.get_child_at(index=0)
        expression = expression_file_util.get_current_expression()
        expected = (
            f'var {child_2.variable_name} = '
            f'{sprite_1.variable_name}.children()[0 + 1];'
        )
        assert expected in expression

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__initialize_children_if_not_initialized(self) -> None:
        child_interface: ChildInterface = ChildInterface()
        child_interface._initialize_children_if_not_initialized()
        assert child_interface._children == []

        stage: Stage = Stage()
        sprite: Sprite = Sprite(stage=stage)
        child_interface._children = Array([sprite])
        child_interface._initialize_children_if_not_initialized()
        assert child_interface._children == [sprite]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__make_snapshot(self) -> None:

        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        sprite_2: Sprite = Sprite(stage=stage)
        sprite_1.add_child(child=sprite_2)
        display_object_1: DisplayObject = DisplayObject(
            stage=stage, variable_name='display_object_1')
        stage.add_child(child=display_object_1)

        snapshot_name_1: str = stage._get_next_snapshot_name()
        stage._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name_1)
        assert stage._children_snapshot[snapshot_name_1] == [
            sprite_1, display_object_1]
        assert stage._is_snapshot_exists(
            snapshot_name=snapshot_name_1)
        assert sprite_1._children_snapshot[snapshot_name_1] == [
            sprite_2]

        stage.remove_child(child=sprite_1)
        stage._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name_1)
        assert stage._children_snapshot[snapshot_name_1] == [
            sprite_1, display_object_1]

    @retry(stop_max_attempt_number=10, wait_fixed=randint(100, 1000))
    def test__revert(self) -> None:
        stage: Stage = Stage()
        sprite_1: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite_1)
        sprite_2: Sprite = Sprite(stage=stage)
        sprite_1.add_child(child=sprite_2)
        display_object_1: DisplayObject = DisplayObject(
            stage=stage, variable_name='display_object_1')
        stage.add_child(child=display_object_1)

        snapshot_name_1: str = sprite_1._get_next_snapshot_name()
        stage._run_all_make_snapshot_methods(
            snapshot_name=snapshot_name_1)
        stage.remove_child(child=sprite_1)
        sprite_1.remove_child(child=sprite_2)
        stage._run_all_revert_methods(snapshot_name=snapshot_name_1)
        assert snapshot_name_1 not in stage._children_snapshot
        assert stage._children == [sprite_1, display_object_1]
        assert sprite_1._children == [sprite_2]
        assert not stage._is_snapshot_exists(
            snapshot_name=snapshot_name_1)
        assert not sprite_1._is_snapshot_exists(
            snapshot_name=snapshot_name_1)

        stage.remove_child(child=sprite_1)
        stage._run_all_revert_methods(snapshot_name=snapshot_name_1)
        assert stage._children == [display_object_1]
