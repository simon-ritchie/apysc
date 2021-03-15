from random import randint

from retrying import retry

from apyscript.display import Sprite
from apyscript.display.display_object import DisplayObject
from apyscript.display.stage import Stage
from apyscript.expression import expression_file_util
from apyscript.type import Array, Boolean, Int
from tests import testing_helper


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
        assert stage._childs == Array([sprite])
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
        assert stage._childs == Array([sprite_1])
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
        sprite: Sprite = Sprite(stage=stage)
        stage.add_child(child=sprite)
        child: DisplayObject = stage.get_child_at(index=0)
        assert child == sprite

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
